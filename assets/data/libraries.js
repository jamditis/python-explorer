// Python Libraries Data
// This file can be easily updated by importing from awesome_python_libraries.json

export const rawLibraries = [
    // WEB DEVELOPMENT
    { n: "Django", c: "Web Frameworks", d: "High-level framework for rapid development and clean design. Batteries-included.", l: "https://www.djangoproject.com/" },
    { n: "Flask", c: "Web Frameworks", d: "Lightweight micro-framework providing core functionality without structure.", l: "https://flask.palletsprojects.com/" },
    { n: "FastAPI", c: "Web Frameworks", d: "Modern, high-performance, async-first web API framework.", l: "https://fastapi.tiangolo.com/" },
    { n: "Pyramid", c: "Web Frameworks", d: "Flexible framework for scaling small web apps into big ones.", l: "https://trypyramid.com/" },
    { n: "Tornado", c: "Web Frameworks", d: "Asynchronous web framework and networking library for real-time services.", l: "https://www.tornadoweb.org/" },
    { n: "Bottle", c: "Web Frameworks", d: "Ultra-minimalist web framework contained in a single file.", l: "https://bottlepy.org/" },
    { n: "CherryPy", c: "Web Frameworks", d: "Object-oriented web framework that allows building apps like standard Python programs.", l: "https://cherrypy.dev/" },
    { n: "Falcon", c: "Web Frameworks", d: "Micro-framework focused on building fast REST APIs with minimal overhead.", l: "https://falconframework.org/" },
    { n: "Masonite", c: "Web Frameworks", d: "Developer-centric, Laravel-inspired framework.", l: "https://docs.masoniteproject.com/" },
    { n: "web2py", c: "Web Frameworks", d: "Full-stack framework with built-in IDE and ticketing system.", l: "http://www.web2py.com/" },
    { n: "Sanic", c: "Web Frameworks", d: "Async Python 3.7+ web server and framework written to go fast.", l: "https://sanic.dev/" },

    // DATA ANALYSIS & SCIENCE
    { n: "Pandas", c: "Data Analysis", d: "High-performance data structures and analysis tools.", l: "https://pandas.pydata.org/" },
    { n: "NumPy", c: "Data Analysis", d: "Fundamental package for scientific computing with N-dimensional arrays.", l: "https://numpy.org/" },
    { n: "SciPy", c: "Science", d: "Algorithms for scientific computing, optimization, and statistics.", l: "https://scipy.org/" },
    { n: "Polars", c: "Data Analysis", d: "Blazingly fast DataFrame library implemented in Rust.", l: "https://pola.rs/" },
    { n: "SQLAlchemy", c: "ORM", d: "SQL toolkit and Object-Relational Mapper for Python.", l: "https://www.sqlalchemy.org/" },
    { n: "Great Expectations", c: "Data Analysis", d: "Framework for validating, documenting, and profiling data.", l: "https://greatexpectations.io/" },

    // DATA ENGINEERING
    { n: "Apache Airflow", c: "Data Engineering", d: "Platform to programmatically author, schedule and monitor workflows.", l: "https://airflow.apache.org/" },
    { n: "Luigi", c: "Data Engineering", d: "Builds pipelines of batch jobs with dependency resolution.", l: "https://github.com/spotify/luigi" },
    { n: "Prefect", c: "Data Engineering", d: "Modern workflow orchestration for data engineering.", l: "https://www.prefect.io/" },
    { n: "Dask", c: "Distributed Computing", d: "Parallel computing library scaling NumPy and Pandas.", l: "https://dask.org/" },
    { n: "PySpark", c: "Distributed Computing", d: "Python API for Apache Spark's distributed processing.", l: "https://spark.apache.org/docs/latest/api/python/" },
    { n: "Ray", c: "Distributed Computing", d: "Distributed execution engine for scaling Python apps.", l: "https://www.ray.io/" },
    { n: "Kafka-Python", c: "Distributed Computing", d: "Tools for real-time data pipelines and streaming.", l: "https://github.com/dpkp/kafka-python" },
    { n: "Faust", c: "Distributed Computing", d: "Stream processing library for Python.", l: "https://faust.readthedocs.io/" },

    // MACHINE LEARNING
    { n: "scikit-learn", c: "Machine Learning", d: "Comprehensive tools for traditional machine learning.", l: "https://scikit-learn.org/" },
    { n: "TensorFlow", c: "Machine Learning", d: "End-to-end open source platform for machine learning.", l: "https://www.tensorflow.org/" },
    { n: "PyTorch", c: "Machine Learning", d: "Dynamic neural networks with strong GPU acceleration.", l: "https://pytorch.org/" },
    { n: "Keras", c: "Machine Learning", d: "High-level neural networks API for fast experimentation.", l: "https://keras.io/" },
    { n: "XGBoost", c: "Machine Learning", d: "Optimized distributed gradient boosting library.", l: "https://xgboost.readthedocs.io/" },
    { n: "LightGBM", c: "Machine Learning", d: "Gradient boosting framework that uses tree-based learning.", l: "https://lightgbm.readthedocs.io/" },
    { n: "spaCy", c: "Natural Language Processing", d: "Industrial-strength Natural Language Processing.", l: "https://spacy.io/" },
    { n: "Hugging Face Transformers", c: "Natural Language Processing", d: "State-of-the-art pre-trained models for NLP and Vision.", l: "https://huggingface.co/docs/transformers/" },
    { n: "OpenCV", c: "Computer Vision", d: "Library mainly aimed at real-time computer vision.", l: "https://opencv.org/" },

    // AUTOMATION
    { n: "Selenium", c: "Automation", d: "Framework for automating web browsers.", l: "https://www.selenium.dev/" },
    { n: "Requests", c: "Automation", d: "Elegant and simple HTTP library for Python.", l: "https://docs.python-requests.org/" },
    { n: "Beautiful Soup", c: "Automation", d: "Library for parsing HTML and XML documents.", l: "https://www.crummy.com/software/BeautifulSoup/" },
    { n: "Scrapy", c: "Automation", d: "High-level web crawling and scraping framework.", l: "https://scrapy.org/" },
    { n: "PyAutoGUI", c: "Automation", d: "Cross-platform GUI automation for mouse and keyboard.", l: "https://pyautogui.readthedocs.io/" },
    { n: "Paramiko", c: "Automation", d: "Implementation of the SSHv2 protocol.", l: "https://www.paramiko.org/" },
    { n: "Fabric", c: "Automation", d: "High-level library for executing shell commands via SSH.", l: "https://www.fabfile.org/" },
    { n: "Celery", c: "Automation", d: "Asynchronous task queue/job queue based on distributed passing.", l: "https://docs.celeryproject.org/" },
    { n: "APScheduler", c: "Automation", d: "In-process task scheduling library.", l: "https://apscheduler.readthedocs.io/" },
    { n: "Robot Framework", c: "Automation", d: "Generic open source automation framework.", l: "https://robotframework.org/" },
    { n: "Pexpect", c: "Automation", d: "Automate interactive console applications.", l: "https://pexpect.readthedocs.io/" },
    { n: "Ansible", c: "Automation", d: "IT automation tool for configuration management.", l: "https://www.ansible.com/" },

    // DESIGN & MEDIA
    { n: "Tkinter", c: "GUI Development", d: "Standard Python interface to the Tk GUI toolkit.", l: "https://docs.python.org/3/library/tkinter.html" },
    { n: "PyQt", c: "GUI Development", d: "Python bindings for the Qt application framework.", l: "https://www.riverbankcomputing.com/software/pyqt/" },
    { n: "PySide", c: "GUI Development", d: "Official Python bindings for the Qt framework.", l: "https://doc.qt.io/qtforpython/" },
    { n: "Kivy", c: "GUI Development", d: "Framework for developing multitouch applications.", l: "https://kivy.org/" },
    { n: "Pygame", c: "Game Development", d: "Modules designed for writing video games.", l: "https://www.pygame.org/" },
    { n: "Pillow", c: "Image Processing", d: "Extensive image processing capabilities.", l: "https://python-pillow.org/" },
    { n: "Blender (bpy)", c: "Design", d: "Scripting and automation for 3D modeling/animation.", l: "https://docs.blender.org/api/current/" },
    { n: "ReportLab", c: "Design", d: "Generate PDFs programmatically.", l: "https://www.reportlab.com/" },
    { n: "Manim", c: "Design", d: "Precise programmatic animations for math education.", l: "https://www.manim.community/" },
    { n: "PyOpenGL", c: "Design", d: "Standard ctypes binding for OpenGL.", l: "http://pyopengl.sourceforge.net/" },
    { n: "VPython", c: "Design", d: "3D programming for ordinary mortals.", l: "https://vpython.org/" },
    { n: "Cairo", c: "Design", d: "Vector graphics library bindings.", l: "https://cairographics.org/" },

    // VISUALIZATION
    { n: "Matplotlib", c: "Data Visualization", d: "Foundational plotting library for Python.", l: "https://matplotlib.org/" },
    { n: "Seaborn", c: "Data Visualization", d: "High-level interface for attractive statistical graphics.", l: "https://seaborn.pydata.org/" },
    { n: "Plotly", c: "Data Visualization", d: "Interactive graphing library for the web.", l: "https://plotly.com/python/" },
    { n: "Bokeh", c: "Data Visualization", d: "Interactive visualization for modern web browsers.", l: "https://bokeh.org/" },
    { n: "Altair", c: "Data Visualization", d: "Declarative statistical visualization library.", l: "https://altair-viz.github.io/" },
    { n: "plotnine", c: "Data Visualization", d: "Implementation of R's ggplot2 grammar of graphics.", l: "https://plotnine.readthedocs.io/" },
    { n: "Dash", c: "Data Visualization", d: "Framework for building analytical web applications.", l: "https://dash.plotly.com/" },
    { n: "HoloViews", c: "Data Visualization", d: "Stop plotting your data - annotate your data and let it visualize itself.", l: "https://holoviews.org/" },
    { n: "Panel", c: "Data Visualization", d: "High-level app and dashboarding solution.", l: "https://panel.holoviz.org/" },
    { n: "Geopandas", c: "Data Visualization", d: "Extends datatypes to spatial operations.", l: "https://geopandas.org/" },
    { n: "NetworkX", c: "Data Visualization", d: "Creation and study of complex networks.", l: "https://networkx.org/" },
    { n: "PyGal", c: "Data Visualization", d: "Sexy python charting.", l: "http://www.pygal.org/" },
    { n: "Mayavi", c: "Data Visualization", d: "3D scientific data visualization and plotting.", l: "https://docs.enthought.com/mayavi/mayavi/" }
];

// Domain mapping for categorization
export const domainMap = {
    "Web Frameworks": "Web", "HTTP Clients": "Web", "Web Content Extracting": "Web",
    "Web Crawling": "Web", "WebSocket": "Web", "WSGI Servers": "Web",
    "Data Analysis": "Data Science", "Science": "Data Science",
    "Data Visualization": "Data Science", "Machine Learning": "Data Science",
    "Deep Learning": "Data Science", "Natural Language Processing": "Data Science",
    "Computer Vision": "Data Science", "Data Engineering": "Data Engineering",
    "ORM": "Data Engineering", "Job Scheduler": "DevOps", "DevOps Tools": "DevOps",
    "Distributed Computing": "DevOps", "Task Queues": "DevOps", "Automation": "DevOps",
    "GUI Development": "Interface", "Game Development": "Interface", "Design": "Media",
    "Image Processing": "Media", "Video": "Media", "Utilities": "Utilities"
};
