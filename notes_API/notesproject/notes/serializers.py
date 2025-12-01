from rest_framework import serializers
from .models import Note, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'color']


class NoteSerializer(serializers.ModelSerializer):
    # Show full tag details when reading
    tags = TagSerializer(many=True, read_only=True)
    # Accept tag IDs when creating/updating
    tag_ids = serializers.PrimaryKeyRelatedField(
        many=True, 
        queryset=Tag.objects.all(), 
        source='tags', 
        write_only=True,
        required=False
    )
    
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'tags', 'tag_ids', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class NoteListSerializer(serializers.ModelSerializer):
    """Lighter serializer for list view - shows only tag names"""
    tags = serializers.StringRelatedField(many=True)
    tag_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Note
        fields = ['id', 'title', 'tags', 'tag_count', 'created_at']
    
    def get_tag_count(self, obj):
        return obj.tags.count()