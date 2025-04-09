from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisteredAssetForm, ClassroomForm, ClassroomAssetForm
from .models import RegisteredAsset, Classroom, ClassroomAsset

# classroom_asset/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisteredAssetForm, ClassroomForm, ClassroomAssetForm
from .models import RegisteredAsset, Classroom, ClassroomAsset

def register_asset(request):
    if request.method == 'POST':
        form = RegisteredAssetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('classroom_list')  # Replace with your list view name
    else:
        form = RegisteredAssetForm()
    return render(request, 'classroom/register_asset.html', {'form': form})

def add_classroom(request):
    if request.method == 'POST':
        form = ClassroomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('classroom_list') # Replace with your list view name
    else:
        form = ClassroomForm()
    return render(request, 'classroom/add_classroom.html', {'form': form})

def assign_asset(request):
    if request.method == 'POST':
        form = ClassroomAssetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('classroom_list') # Replace with your list view name
    else:
        form = ClassroomAssetForm()
    return render(request, 'classroom/assign_asset.html', {'form': form})

def classroom_list(request):
    classrooms = Classroom.objects.all()
    classroom_assets = ClassroomAsset.objects.all()
    registered_assets = RegisteredAsset.objects.all()
    return render(request, 'classroom/classroom_list.html', {'classrooms': classrooms, 'classroom_assets': classroom_assets, 'registered_assets': registered_assets})

def edit_asset(request, asset_id):
    asset = get_object_or_404(RegisteredAsset, pk=asset_id)
    if request.method == 'POST':
        form = RegisteredAssetForm(request.POST, instance=asset)
        if form.is_valid():
            form.save()
            return redirect('classroom_list')  # Replace with your list view name
    else:
        form = RegisteredAssetForm(instance=asset)
    return render(request, 'classroom/edit_asset.html', {'form': form, 'asset': asset})

def edit_classroom(request, classroom_id):
    classroom = get_object_or_404(Classroom, pk=classroom_id)
    if request.method == 'POST':
        form = ClassroomForm(request.POST, instance=classroom)
        if form.is_valid():
            form.save()
            return redirect('classroom_list')
    else:
        form = ClassroomForm(instance=classroom)
    return render(request, 'classroom/edit_classroom.html', {'form': form, 'classroom': classroom})

def edit_classroom_asset(request, classroom_asset_id):
    classroom_asset = get_object_or_404(ClassroomAsset, pk=classroom_asset_id)
    if request.method == 'POST':
        form = ClassroomAssetForm(request.POST, instance=classroom_asset)
        if form.is_valid():
            form.save()
            return redirect('classroom_list')
    else:
        form = ClassroomAssetForm(instance=classroom_asset)
    return render(request, 'classroom/edit_classroom_asset.html', {'form': form, 'classroom_asset': classroom_asset})

def delete_asset(request, asset_id):
    asset = get_object_or_404(RegisteredAsset, pk=asset_id)
    if request.method == 'POST':
        asset.delete()
        return redirect('classroom_list')
    return render(request, 'classroom/delete_asset.html', {'asset': asset})

def delete_classroom(request, classroom_id):
    classroom = get_object_or_404(Classroom, pk=classroom_id)
    if request.method == 'POST':
        classroom.delete()
        return redirect('classroom_list')
    return render(request, 'classroom/delete_classroom.html', {'classroom': classroom})

def delete_classroom_asset(request, classroom_asset_id):
    classroom_asset = get_object_or_404(ClassroomAsset, pk=classroom_asset_id)
    if request.method == 'POST':
        classroom_asset.delete()
        return redirect('classroom_list')
    return render(request, 'classroom/delete_classroom_asset.html', {'classroom_asset': classroom_asset})