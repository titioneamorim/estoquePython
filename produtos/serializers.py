from django.db import models
from django.db.models import fields
from rest_framework.utils import field_mapping
from .models import ProdutoModel
from rest_framework import serializers

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdutoModel
        fields = '__all__'
        