from decimal import Decimal
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.shortcuts import render
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.utils import simplejson as json, simplejson

import base64
import hashlib
import hmac
import urllib2
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
import datetime
from Perfumes.models import PerfumeLinkDetail,Question


@csrf_exempt
#@facebook_authorization_required()
def show_contest(request, template="base.html"):
      data=parse_signed_request(
             request.REQUEST.get('signed_request') or request.COOKIES.get('signed_request'),
            "83083ed799af7cf928ba64f3b7ee754e"
        )
      ctx={}
      ctx['page']=bool(0)
      if data:
          if 'page' in data.keys():
             ctx['page']=bool(1)
      return render_to_response(template,ctx, context_instance=RequestContext(request))

def get_selected_perfume_info(request):
    selected_option=request.GET['selected_option']
    gender=request.GET['gender']
    print selected_option
    perfumes_obj = PerfumeLinkDetail.objects.filter(gender=gender, is_enabled=True, link_weight=selected_option).order_by('?')[:1]
    print perfumes_obj
    perfume = {}
    for perfume_obj in perfumes_obj:
        perfume["title"] = perfume_obj.title
        perfume["caption"] = perfume_obj.caption
        perfume["image"]  =perfume_obj.image_link
        perfume["description"] = perfume_obj.description
        perfume["weblink"]     = perfume_obj.weblink
        print perfume
    return HttpResponse(json.dumps(perfume), mimetype="application/json")

def base64_url_decode(inp):
    padding_factor = (4 - len(inp) % 4) % 4
    inp += "="*padding_factor
    return base64.b64decode(unicode(inp).translate(dict(zip(map(ord, u'-_'), u'+/'))))

def parse_signed_request(signed_request, secret):
    if signed_request is None:
        return None

    l = signed_request.split('.', 2)
    encoded_sig = l[0]
    payload = l[1]

    sig = base64_url_decode(encoded_sig)
    data = json.loads(base64_url_decode(payload))

    if data.get('algorithm').upper() != 'HMAC-SHA256':
        #log.error('Unknown algorithm')
        return None
    else:
        expected_sig = hmac.new(secret, msg=payload, digestmod=hashlib.sha256).digest()

    if sig != expected_sig:
        return None
    else:
        #log.debug('valid signed request received..')
        return data


