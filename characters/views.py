from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CharacterSheet
from .forms import CharacterSheetForm

@login_required
def character_sheet_list(request):
    character_sheets = CharacterSheet.objects.filter(user=request.user)
    return render(request, 'character_sheet_list.html', {'character_sheets': character_sheets})

@login_required
def character_sheet_edit(request, pk):
    character_sheet = CharacterSheet.objects.get(pk=pk)
    if request.method == 'POST':
        form = CharacterSheetForm(request.POST, instance=character_sheet)
        if form.is_valid():
            form.save()
            return redirect('character_sheet_list')
    else:
        form = CharacterSheetForm(instance=character_sheet)
    return render(request, 'character_sheet_edit.html', {'form': form})

@login_required
def character_sheet_new(request):
    if request.method == 'POST':
        form = CharacterSheetForm(request.POST)
        if form.is_valid():
            character_sheet = form.save(commit=False)
            character_sheet.user = request.user
            character_sheet.save()
            return redirect('character_sheet_list')
    else:
        form = CharacterSheetForm()
    return render(request, 'character_sheet_edit.html', {'form': form})