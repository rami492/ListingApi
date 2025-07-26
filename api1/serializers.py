from rest_framework import serializers
from django.contrib.auth.models import User
from  api1.models import Listing
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from rest_framework.decorators import action

class ListingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Listing
        fields = ['id', 'title', 'owner']

class UserSerializer(serializers.ModelSerializer):
    listings = serializers.PrimaryKeyRelatedField(many=True, queryset=Listing.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'listings']

class CreateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
        )
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'password2', 'email', 'first_name', 'last_name']
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    

class LoginSerlializer(serializers.Serializer):
    #email = serializers.EmailField(
    #    required=True,
    #)
    username = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True, required=True)

    def validate(self, attrs):

        if User.objects.filter(username=attrs.get('username')).exists():
            user = authenticate(request=self.context.get('request'), username=attrs.get('username'), password=attrs.get('password'))
            attrs['user'] = user
            if user:
                return attrs
            else:
                raise serializers.ValidationError({"password": "fields didn't match."})
        raise serializers.ValidationError({"username": "fields didn't match."})