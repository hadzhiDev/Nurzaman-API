from rest_framework import serializers

from main.models import Apartment, Block, Object


class ObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Object
        fields = '__all__'


class BlockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Block
        fields = '__all__'


class ApartmentListSerializer(serializers.ModelSerializer):
    block = BlockSerializer(many=False)

    class Meta:
        model = Apartment
        fields = ('id', 'number', 'floor', 'area', 'image', 'rooms_count', 'block')


class ApartmentDetailSerializer(serializers.ModelSerializer):
    block_name = serializers.CharField(source='block.name', read_only=True)
    block_id = serializers.IntegerField(source='block.id', read_only=True)
    object_name = serializers.CharField(source='block.object.name', read_only=True)

    class Meta:
        model = Apartment
        fields = '__all__'


class ApartmentCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = '__all__'


# class ApartmentSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     number = serializers.IntegerField()
#     floor = serializers.IntegerField()
#     rooms_count = serializers.IntegerField()
#     area = serializers.FloatField()
#     image = serializers.ImageField(required=False, allow_null=True)
#     block = serializers.PrimaryKeyRelatedField(queryset=Block.objects.all(), required=False, allow_null=True)

#     def validate(self, attrs):
#         print(attrs.get("number"))
#         print(attrs)
#         if attrs.get("area") >= 500:
#             raise serializers.ValidationError("Area too large")
#         return super().validate(attrs)
    
#     def create(self, validated_data):
#         print(validated_data)
#         return Apartment.objects.create(**validated_data)
    
#     def update(self, instance, validate_data):
#         instance.number = validate_data.get('number', instance.number)
#         instance.floor = validate_data.get('floor', instance.floor)
#         instance.rooms_count = validate_data.get('rooms_count', instance.rooms_count)
#         instance.area = validate_data.get('area', instance.area)
#         instance.image = validate_data.get('number', instance.image)
#         instance.save()
#         return instance





class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=100)
    new_password = serializers.CharField(max_length=100)
    confirm_password = serializers.CharField(max_length=100)

    def validate(self, attrs):
        
        return super().validate(attrs)