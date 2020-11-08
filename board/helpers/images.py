import os


def get_upload_path(instance, filename):
    return os.path.join('images/',
                        "user_%d" % instance.post.user.id, "photo_%s" % filename)
