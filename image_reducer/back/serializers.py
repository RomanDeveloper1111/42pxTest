from rest_framework import serializers
from back.models import Reducer
from PIL import Image
from back.handlers import upload_to


class ReduceSerializer(serializers.ModelSerializer):
    width = serializers.CharField(max_length=4)
    height = serializers.CharField(max_length=4, required=False)

    class Meta:
        model = Reducer
        fields = ['image', 'width', 'height']
        read_only_fields = ['natural_image_name', ]

    def validate(self, data):
        with Image.open(data['image']) as img:
            if img.format.lower() not in ['jpeg', 'jpg', 'png']:
                raise serializers.ValidationError('Wrong image format!')

        if int(data['width']) <= 0:
            raise serializers.ValidationError('Width can not be less or equals than 0! ')

        if 'height' in data.keys() and int(data['height']) <= 0:
            raise serializers.ValidationError('Height can not be less or equals than 0! ')

        return data

    def create(self, validated_data):
        image = validated_data.pop('image')
        validated_data['natural_image_name'] = image

        width = int(validated_data.pop('width'))
        height = width
        if 'height' in validated_data.keys():
            height = int(validated_data.pop('height'))

        instance = Reducer.objects.create(**validated_data)
        new_filename = upload_to(None, image.name, width, height)

        with Image.open(image) as img:
            new_image = img.resize(size=(width, height))
            new_image.save('media/' + new_filename)

        instance.image = new_filename

        instance.save()

        return instance
