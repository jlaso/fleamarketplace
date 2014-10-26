from django.forms import widgets
from rest_framework import serializers
from models import Market


class MarketSerializer(serializers.Serializer):
    pk = serializers.Field()  # Note: `Field` is an untyped read-only field.
    name = serializers.CharField(required=False,
                                  max_length=100)
    address = serializers.CharField(widget=widgets.Textarea,
                                 max_length=100000)
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new snippet instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            instance.name = attrs.get('name', instance.title)
            instance.address = attrs.get('address', instance.code)
            instance.latitude = attrs.get('latitude', instance.linenos)
            instance.longitude = attrs.get('longitude', instance.language)
            return instance

        # Create new instance
        return Market(**attrs)