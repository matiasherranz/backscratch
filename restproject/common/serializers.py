
from django.contrib.auth.models import User, Group

from rest_framework import serializers

from common.models import BackScratcher


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class BackScratcherSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(
        required=True, allow_blank=False, max_length=80
    )
    description = serializers.CharField(required=False)
    size = serializers.ChoiceField(choices=BackScratcher.SIZES, default='M')
    price = serializers.FloatField(required=True)

    def create(self, validated_data):
        """
        Create and return a new `BackScratcher` instance,
        given the validated data.
        """
        return BackScratcher.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `BackScratcher` instance,
        given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get(
            'description', instance.description
        )
        instance.size = validated_data.get('size', instance.size)
        instance.price = validated_data.get('price', instance.price)
        instance.save()

        return instance
