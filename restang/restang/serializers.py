from rest_framework import serializers

from restang.models import RestangElements

class RestangSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestangElements
        fields = 'id', 'restang_text', 'done'
