from django.shortcuts import render
from django.shortcuts import redirect,render
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError
from.models import File
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import matplotlib
matplotlib.use('Agg')

# Create your views here.


def index(request):
    if request.method == "POST":
        try:
            file = request.FILES['file']
            file_instance = File.objects.create(file=file)
            messages.success(request, 'File Uploaded Successfully')
            return redirect('analysis', file_id=file_instance.id)
        
        except MultiValueDictKeyError:
            messages.error(request, 'No file was uploaded')
    
    
    return render(request,'index.html')


def analysis(request, file_id):
    file_instance = File.objects.get(id=file_id)
    df = pd.read_csv(file_instance.file.path)

    # Perform basic data analysis
    head = df.head().to_html()
    description = df.describe().to_html()
    missing_values = df.isnull().sum().to_frame(name='Missing Values').to_html()


    hist_dir = os.path.join('app', 'static')
    # Generate plots
    plt.figure(figsize=(10, 6))
    sns.histplot(df.select_dtypes(include=['float64', 'int64']).iloc[:, 0])
    plt.title('Histogram')
    
    
    
    hist_path = os.path.join(hist_dir, f'histogram_{file_id}.png')
    plt.savefig(hist_path)
    plt.clf()

    context = {
        'head': head,
        'description': description,
        'missing_values': missing_values,
        'histogram': f'histogram_{file_id}.png'
    }
    return render(request, 'analysis.html', context)