import io
import zipfile as zip

# Create your views here.
from PIL import Image, ImageFile
from PIL.GifImagePlugin import GifImageFile
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

ImageFile.LOAD_TRUNCATED_IMAGES = True


def GifToImglist(gif):
    '''
    :type gif:GifImageFile
    :return:
    '''
    plist = []
    frame = 0
    while gif:
        frame += 1
        buf = io.BytesIO()
        gif.save(buf, "GIF")
        plist.append(buf.getbuffer().tobytes())
        try:
            gif.seek(frame)
        except EOFError:
            break
    return plist


class GifExtract(View):

    def get(self, req, id=0):
        return render(req, "index.html", {
            "title": "Hello world.",
            "message": "This is a test page."
        })

    def post(self, req):
        fp = io.BytesIO(req.body)
        x = Image.open(fp)
        plist = GifToImglist(x)

        zipio = io.BytesIO()
        with zip.ZipFile(zipio, "w") as z:
            for idx, img in enumerate(plist):
                z.writestr("%d.gif" % idx, img)

        return HttpResponse(zipio.getbuffer().tobytes(), content_type="application/zip")

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(GifExtract, self).dispatch(*args, **kwargs)
