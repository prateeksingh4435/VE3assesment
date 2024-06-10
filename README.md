# First we have to create a project and an app :
                                    django-admin startproject assesment
                                    cd assesment
                                    python manage.py startapp app

# Go to the settings.py file and add this app under installed apps 

![image](https://github.com/prateeksingh4435/VE3assesment/assets/128826031/0f365450-2206-47c9-9a05-1d08ebd68573)

# Create a Model where we store our CSV file in backend 
![image](https://github.com/prateeksingh4435/VE3assesment/assets/128826031/9a36124c-b58c-4343-94df-6d2ae559ff5a)

# Create a HTML template form where we upload our CSV file 
![image](https://github.com/prateeksingh4435/VE3assesment/assets/128826031/dce4c19b-9f1c-4c85-a1e3-47e7afb2678c)

# Logic to save and store our CSV file :
The index view function handles requests to the index page. If the request method is POST, 
it attempts to retrieve an uploaded file from the request. If successful, it creates a new File object with the uploaded file and
redirects the user to the analysis page with the ID of the newly created file. If no file is uploaded, it displays an error message.
In either case, it renders the index.html template, allowing users to upload files via a form.
                           
![image](https://github.com/prateeksingh4435/VE3assesment/assets/128826031/27311932-7d10-4b4f-aad9-51cb6cdfa305)



# file_instance = File.objects.get(id=file_id) :
This line retrieves the file instance associated with the given file_id from the database.
# df = pd.read_csv(file_instance.file.path) :
This line reads the CSV file associated with the file instance (file_instance) and creates a DataFrame (df) using pandas' read_csv function.
# head = df.head().to_html() :
This line generates an HTML representation of the first few rows of the DataFrame (df) using the head() method, which by default returns the first 5 rows.
The .to_html() method converts the DataFrame into an HTML table.

# description = df.describe().to_html() :
This line computes summary statistics for numerical columns in the DataFrame (df) using the describe() method and converts the result into an HTML table 
using .to_html().
# missing_values = df.isnull().sum().to_frame(name='Missing Values').to_html() :
 This line calculates the count of missing values for each column in the DataFrame (df) using isnull().sum() and converts the result into an HTML table with a column named 'Missing Values'
   using .to_frame(name='Missing Values').to_html().

# hist_dir = os.path.join('app', 'static') :
This line constructs the path to the directory where the histogram image will be saved. It joins the 'app' directory and the 'static' directory using os.path.join().
# plt.figure(figsize=(10, 6)) sns.histplot(df.select_dtypes(include=['float64', 'int64']).iloc[:, 0]) plt.title('Histogram') : 
These lines create a histogram using seaborn (sns) based on the first numerical column in the DataFrame (df). plt.figure(figsize=(10, 6)) sets the figure size to 10x6 inches. plt.title('Histogram') sets the title of the histogram.

# hist_path = os.path.join(hist_dir, f'histogram_{file_id}.png')
# plt.savefig(hist_path)
# plt.clf() :
These lines save the histogram plot as a PNG image in the directory specified by hist_dir with a filename formatted as 'histogram_file_id.png'.
After saving the plot, plt.clf() clears the current figure to release memory resources.
# context = {
    'head': head,
    'description': description,
    'missing_values': missing_values,
    'histogram': f'histogram_{file_id}.png'
}
This dictionary (context) contains the data to be passed to the template. It includes HTML representations of the DataFrame's first few rows, summary statistics, missing values, and the filename of the histogram image.


# Working Demo OF the Assesment 
![image](https://github.com/prateeksingh4435/VE3assesment/assets/128826031/69ebe131-d55b-4de0-933c-b3a006eb80b2)

![image](https://github.com/prateeksingh4435/VE3assesment/assets/128826031/6ff0787e-bda1-4851-aae3-8cf7900e1ce0)

# Analysis of the CSV file
![image](https://github.com/prateeksingh4435/VE3assesment/assets/128826031/c6367158-04af-4bda-bc02-38ee8c72a8a4)

![image](https://github.com/prateeksingh4435/VE3assesment/assets/128826031/898877aa-f5a9-4d2c-979d-a6167734ab29)

![image](https://github.com/prateeksingh4435/VE3assesment/assets/128826031/85ed318a-387c-479c-a6ac-1ff17e29e9c1)

