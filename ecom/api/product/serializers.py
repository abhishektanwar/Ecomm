from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
	# in django image doesnt give us full url that is why serialized for
	# image is being used here
	image = serializers.ImageField(max_length = None, allow_empty_file=False, allow_null = True, required=False)	
	class Meta:
		model = Product
		fields = (
			'id','name','description','price','stock','image','category'
		)