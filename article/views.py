from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from article.forms import ArticleForm
from article.models import ArticleEntry
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.utils.html import strip_tags
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import HttpResponseForbidden
import json
from django.http import JsonResponse

# show article
def article_list(request):
    article_entries = ArticleEntry.objects.all()
    context = {
        'article_entries': article_entries,
    }
    return render(request, 'article_list.html', context)

def article_detail(request, id):
    article_entry = get_object_or_404(ArticleEntry, id=id)
    return render(request, 'article_detail.html', {'article_entry': article_entry})

@login_required(login_url='login/')
def create_article(request):
    form = ArticleForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        article_entry = form.save(commit=False)
        article_entry.user = request.user
        form.save()
        return redirect('article:article_list')
    
    context = {'form':form}
    return render(request, 'create_article.html', context)

def show_xml(request):
    data = ArticleEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = ArticleEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = ArticleEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = ArticleEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
@require_POST
def create_article_ajax(request):
    if request.method == 'POST':
        title = strip_tags(request.POST.get('title'))
        content = strip_tags(request.POST.get('content'))
        image_url = strip_tags(request.POST.get('image_url'))
        article_entry = ArticleEntry.objects.create(
            title=title,
            content=content,
            image_url=image_url,
            user=request.user,
        )
        data = serializers.serialize('json', [article_entry])
        return JsonResponse({'article': data})
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)

login_required
def edit_article(request, id):
    article_entry = get_object_or_404(ArticleEntry, id=id)
    if article_entry.user != request.user:
        return HttpResponseForbidden("Anda tidak diizinkan untuk mengedit artikel ini.")

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article_entry)
        if form.is_valid():
            form.save()
            return redirect('article:article_list')
    else:
        form = ArticleForm(instance=article_entry)

    return render(request, 'edit_article.html', {'form': form})

# View untuk menghapus artikel
@login_required
def delete_article(request, id):
    article_entry = get_object_or_404(ArticleEntry, id=id)
    if article_entry.user != request.user:
        return HttpResponseForbidden("Anda tidak diizinkan untuk menghapus artikel ini.")

    if request.method == 'POST':
        article_entry.delete()
        return redirect('article:article_list')

    return render(request, 'confirm_delete.html', {'article_entry': article_entry})

@csrf_exempt
def create_article_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = request.user if request.user.is_authenticated else None

        new_article = ArticleEntry.objects.create(
            user=user,  # atau None jika belum login
            title=data.get('title', ''),
            content=data.get('content', ''),
            image_url=data.get('image_url', '') or None,
        )
        new_article.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    
@csrf_exempt
def delete_article_flutter(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            article_id = data.get('id', None)

            if not article_id:
                return JsonResponse({"status": "error", "message": "ID artikel diperlukan."}, status=400)

            article = ArticleEntry.objects.filter(id=article_id).first()

            if article is None:
                return JsonResponse({"status": "error", "message": "Artikel tidak ditemukan."}, status=404)

            article.delete()
            return JsonResponse({"status": "success", "message": "Artikel berhasil dihapus."}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON."}, status=400)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
    else:
        return JsonResponse({"status": "error", "message": "Hanya menerima POST request."}, status=405)

@csrf_exempt
def edit_article_flutter(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            article_id = data.get('id', None)

            if not article_id:
                return JsonResponse({"status": "error", "message": "ID artikel diperlukan."}, status=400)

            article = ArticleEntry.objects.filter(id=article_id).first()

            if article is None:
                return JsonResponse({"status": "error", "message": "Artikel tidak ditemukan."}, status=404)

            # Update field jika ada dalam data
            title = data.get('title', '').strip()
            content = data.get('content', '').strip()
            image_url = data.get('image_url', '').strip()

            if title:
                article.title = title
            if content:
                article.content = content
            if image_url:
                article.image_url = image_url
            elif 'image_url' in data and not image_url:
                # Jika 'image_url' disertakan dan kosong, hapus URL gambar
                article.image_url = None

            article.save()

            article_data = {
                'id': article.id,
                'title': article.title,
                'content': article.content,
                'image_url': article.image_url,
                'published_date': article.published_date,
                'user': article.user.username if article.user else None,
            }

            return JsonResponse({
                "status": "success",
                "message": "Artikel berhasil diperbarui.",
                "article": article_data
            }, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON."}, status=400)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
    else:
        return JsonResponse({"status": "error", "message": "Hanya menerima POST request."}, status=405)