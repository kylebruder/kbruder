from django.db.models.signals import post_save
from django.dispatch import receiver
from pathlib import Path
from PIL import Image as img
from PIL import ImageOps
from images.models import Image

@receiver(post_save, sender=Image)
def add_thumbnail(sender, instance, created, **kwargs):
    '''
    Add a thumbnail image to the Image model after it is saved to DB
    '''
    if created:
        upload_dir = instance.creation_date.strftime(
            'media/images/%Y/%m/%d/'
        )
        p = Path('media')
        q = p / instance.image_file.name
        image = img.open(q)
        # Transpose Exif tags if the image has them
        try:
            image = ImageOps.exif_transpose(image)
            image.save(q)
        except:
            pass
        max_size = (200, 200)
        image.thumbnail(max_size)
        thumb_dir = instance.creation_date.strftime(
            'images/thumbnails/%Y/%m/%d/'
        )
        file_name = instance.image_file.name.split('/')[-1].split('.')[0]
        extension = instance.image_file.name.split('/')[-1].split('.')[-1]
        thumb_file_name = '{}{}{}'.format(file_name, '-thumbnail.', extension)
        p = Path('media')
        q = p / thumb_dir
        Path.mkdir(q, parents=True, exist_ok=True)
        image.save(q / thumb_file_name)
        image.close()
        p = Path(thumb_dir)
        q = p / thumb_file_name
        instance.thumbnail_file = str(q)
        instance.save()

