#!/usr/bin/env python3
"""
Merge enhanced descriptions from all batches back into libraries.js
Also adds journalism/media relevance tags
"""

import json
import re

# All enhanced descriptions from the 7 batches
enhanced_descriptions = {
    # Batch 1
    "ajenti": "A web-based admin dashboard that makes it easy to manage and monitor your servers without using complicated command-line tools.",
    "django-grappelli": "Makes Django's admin interface look prettier and more modern so it's nicer to use for managing your website's data.",
    "flask-admin": "Quickly create an admin panel for your Flask web app to manage your data without building one from scratch.",
    "flower": "A web interface to watch what's happening with your background tasks in Celery and see if they're running smoothly.",
    "jet-bridge": "Automatically generate a polished admin panel for any Python application so you can manage your data through a nice interface.",
    "wooey": "Turn your Python scripts into interactive web forms so anyone can use them without touching the command line.",
    "streamlit": "Build interactive dashboards and data apps in minutes using simple Python code, perfect for sharing analysis and reports.",
    "daphne": "A fast server that runs modern web applications built with Django, handling real-time features like WebSockets.",
    "uvicorn": "An extremely fast web server that runs modern Python web frameworks, built for speed and performance.",
    "hypercorn": "A flexible web server similar to Gunicorn but designed to work with newer Python web frameworks for better performance.",
    "asyncio": "Python's built-in tool for writing programs that handle many tasks at once, like talking to multiple users or services simultaneously.",
    "concurrent.futures": "A built-in Python tool that lets you run multiple tasks at the same time to make your programs faster and more responsive.",
    "multiprocessing": "Python's standard way to split work across multiple processor cores, letting you do heavy computations much faster.",
    "trio": "A friendly library for writing programs that do multiple things at once, with clearer and easier-to-understand code than asyncio.",
    "twisted": "A powerful framework for building programs that handle many network connections at once, like chat servers or web scrapers.",
    "uvloop": "A super-fast replacement for Python's async engine that makes your concurrent programs run significantly faster.",
    "eventlet": "A library that lets you handle many network connections at once without writing complicated async code.",
    "gevent": "A library that makes it easy to write programs handling many tasks simultaneously using lightweight threads.",
    "bitbake": "A build tool designed for creating custom embedded Linux systems, similar to Make but specifically for Linux projects.",
    "buildout": "A tool that automates building and assembling complex applications made of many separate parts.",
    "platformio": "Helps you write and compile code for embedded devices like Arduino and microcontrollers in a unified way.",
    "pybuilder": "An automation tool for building Python projects, handling tests, packaging, and publishing all in one place.",
    "scons": "A powerful build tool that automates compiling code and managing project dependencies across different systems.",
    "attrs": "Reduces boilerplate code in Python classes by automatically generating common methods like __init__ and __repr__.",
    "bidict": "A specialized dictionary that lets you look up values in both directions, useful for maintaining two-way relationships.",
    "box": "A Python dictionary that lets you access items using dot notation (like obj.key) instead of bracket notation (like obj['key']).",
    "dataclasses": "Python's built-in way to create simple classes for storing data with automatic methods for initialization and representation.",
    "dotteddict": "Lets you access nested dictionaries and lists using dot notation, like accessing 'config.database.host' as a path.",
    "feincms": "A powerful content management system built on Django for creating and managing website content without coding.",
    "indico": "A full-featured event management system for planning conferences, meetings, and gatherings with registration and scheduling.",
    "wagtail": "A content management system for Django that makes it easy to create and edit website pages with a user-friendly interface.",
    "beaker": "A web middleware that handles storing user session data and caching information to make websites faster.",
    "django-cache-machine": "Automatically stores Django database results in cache and updates the cache when data changes, improving performance.",
    "django-cacheops": "A smart caching tool for Django that automatically figures out what to refresh when your data changes.",
    "dogpile.cache": "A modern caching library that works with databases and web frameworks to speed up your application.",
    "hermescache": "A Python caching system that organizes cached data with tags so you can selectively refresh only what you need.",
    "pylibmc": "A Python connection to Memcached, a popular tool for temporarily storing data to make websites run much faster.",
    "python-diskcache": "Stores cached data on disk using a database, offering better performance and persistence than traditional memory caches.",
    "errbot": "A chatbot framework that lets you automate tasks through chat platforms, enabling team automation and notifications.",
    "easyocr": "Extracts text from images automatically, supporting over 40 languages with minimal setup or configuration needed.",
    "kornia": "A computer vision library for PyTorch that provides advanced image processing tools for machine learning projects.",
    "opencv": "A comprehensive library for image and video processing, used for everything from face detection to video analysis.",
    "pytesseract": "A simple Python wrapper around Google's Tesseract tool for converting images and scanned documents into readable text.",
    "tesserocr": "An alternative wrapper for Tesseract OCR that's easy to use with image libraries and works well for text extraction.",
    "configparser": "Python's built-in tool for reading and writing configuration files (INI format), making your apps customizable.",
    "configobj": "Reads configuration files with the ability to validate the values, ensuring your settings are correct before use.",
    "hydra": "A framework that makes managing complex application settings easy, especially useful for machine learning experiments.",
    "python-decouple": "Keeps sensitive information like passwords and API keys separate from your code using environment variables.",
    "cryptography": "Provides tools for encrypting and decrypting data, creating secure communication channels, and protecting sensitive information.",
    "paramiko": "Lets you connect to remote servers and run commands over SSH directly from Python, automating server management tasks.",

    # Batch 2
    "pynacl": "A library for keeping your data secure by encrypting and decrypting information so only the right people can read it.",
    "pandas": "Makes it easy to work with spreadsheet-like data in Python—sort it, filter it, analyze it, and create charts all in code.",
    "aws-sdk-pandas": "Lets you use pandas to work directly with data stored on Amazon Web Services without downloading it first.",
    "datasette": "A tool that lets you explore databases and publish them on the web so others can search and analyze your data.",
    "desbordante": "Automatically examines your data to find patterns, errors, and relationships you might have missed manually.",
    "optimus": "Makes it simpler to process really large amounts of data using PySpark without getting bogged down in complex code.",
    "cerberus": "Checks if your data is correct and matches the rules you set up before you use or save it.",
    "colander": "Takes messy data from websites or APIs, checks if it's valid, and converts it into clean Python data you can use.",
    "jsonschema": "Verifies that JSON data (common format from APIs) matches the structure and rules you expect.",
    "schema": "A simple way to define and check that Python data structures (lists, dictionaries) have the right shape and types.",
    "schematics": "Validates and transforms data into proper formats, useful when handling information from forms or APIs.",
    "voluptuous": "Makes sure your Python data is correct by checking it against rules you define in an easy-to-read way.",
    "pydantic": "Uses Python's type hints to automatically validate and convert your data into the correct types.",
    "altair": "Create beautiful, interactive charts and graphs from your data using simple, readable code.",
    "bokeh": "Make interactive web-based charts and visualizations that users can zoom, pan, and explore in their browser.",
    "bqplot": "Create interactive graphs directly inside Jupyter notebooks that you can click and explore.",
    "cartopy": "Draw maps and geographic data visualizations so you can display information on real-world locations.",
    "diagrams": "Generate professional system diagrams (like architecture or flowcharts) by writing code instead of using drawing tools.",
    "matplotlib": "Python's go-to library for making all kinds of plots, charts, and graphs to visualize your data.",
    "plotnine": "Create beautiful charts using a grammar-of-graphics approach similar to R's ggplot2.",
    "pygal": "Generate clean, scalable charts as SVG files that look great on websites and in documents.",
    "pygraphviz": "Visualize networks, graphs, and relationships using the powerful Graphviz layout engine from Python.",
    "pyqtgraph": "Build real-time, interactive scientific plots and dashboards with fast performance for live data.",
    "seaborn": "Makes statistical charts and plots look beautiful and professional with just a few lines of code.",
    "vispy": "Create extremely fast, high-quality 3D and scientific visualizations using your computer's graphics card.",
    "pickleDB": "A lightweight database that stores key-value pairs (like a dictionary) without needing complex setup.",
    "tinydb": "A lightweight database perfect for small projects where you want to store and query documents without SQL.",
    "zodb": "Store Python objects directly in a database without having to convert them to SQL or JSON first.",
    "arrow": "Work with dates and times in Python in a much simpler, more intuitive way than the built-in tools.",
    "dateutil": "Extends Python's date/time tools with extra features like parsing dates in any format and handling timezones.",
    "pendulum": "Simplifies working with dates and times in Python, making timezone handling and date math much easier.",
    "pytz": "Handles all the world's timezones so you can work with dates correctly no matter where users are located.",
    "keras": "A beginner-friendly library for building artificial neural networks (AI models) with simple, readable code.",
    "pytorch": "A powerful library for building and training AI models with the speed and flexibility that researchers love.",
    "pytorch-lightning": "Streamlines the process of training AI models in PyTorch, handling tedious details so you focus on your model.",
    "stable-baselines3": "Pre-built algorithms for training AI agents to learn tasks through trial and error (reinforcement learning).",
    "tensorflow": "Google's industry-standard library for building, training, and deploying machine learning and AI models at scale.",
    "theano": "A library designed for fast mathematical computations on large arrays, often used for deep learning research.",
    "py2app": "Convert your Python script into a standalone app that Mac users can run without needing Python installed.",
    "py2exe": "Convert your Python script into a standalone .exe file so Windows users can run it without installing Python.",
    "pyarmor": "Protects your Python code by encrypting it so people can't easily read or modify what you've written.",
    "pyinstaller": "Convert your Python scripts into executable files that work on Windows, Mac, or Linux without needing Python installed.",
    "shiv": "Bundle your Python program with all its dependencies into a single file that runs anywhere.",
    "sphinx": "Automatically generate professional documentation for your Python code from docstrings and markdown files.",
    "pdoc": "Quickly generate clean, readable API documentation for your Python library with minimal setup.",
    "akshare": "Access financial market data (stocks, crypto, bonds) easily from Chinese and international sources.",
    "s3cmd": "A command-line tool for uploading, downloading, and managing files stored on Amazon's S3 cloud storage.",
    "youtube-dl": "Download videos from YouTube and other video websites directly from the command line.",
    "pyenv": "Easily switch between different Python versions on your computer without conflicts or complicated setup.",
    "virtualenv": "Create isolated Python environments on your computer so different projects don't interfere with each other's packages.",

    # Batch 3
    "mimetypes": "Automatically identifies what type of file you're dealing with by looking at its name or content, so your program knows whether it's handling a picture, document, video, etc.",
    "pathlib": "Makes it easy to work with file and folder paths in your code without worrying about whether you're on Windows, Mac, or Linux—it handles the differences automatically.",
    "path.py": "Simplifies working with file paths by providing a cleaner, more intuitive way to navigate and manipulate files and folders in your Python code.",
    "python-magic": "Detects what type of file you have by examining its actual content rather than just its extension, making it harder to fool with mislabeled files.",
    "watchdog": "Lets your program automatically detect and react when files change, get created, or deleted in a folder without constantly checking—perfect for auto-saving or syncing tools.",
    "coconut": "An alternative Python syntax that makes it easier and cleaner to write certain types of code, especially when you want a more functional programming style.",
    "funcy": "Provides handy shortcuts and tools for working with data in creative ways, making complex operations simpler and more readable.",
    "more-itertools": "Offers extra power tools for looping through and manipulating lists and data collections beyond what Python provides built-in.",
    "returns": "Helps you write more predictable, safer code by providing organized ways to handle different outcomes (success, failure, or special cases) without catching exceptions.",
    "cytoolz": "A super-fast version of functional programming tools that uses compiled code under the hood for handling large datasets without slowing down.",
    "toolz": "A collection of helper functions for working with lists, dictionaries, and data transformations in a clean, functional programming style.",
    "curses": "Lets you build text-based, interactive user interfaces in the terminal with windows, buttons, and menus—great for command-line tools.",
    "Eel": "Combines Python code with web technologies to create desktop applications that look modern and work offline without needing an internet connection.",
    "enaml": "Makes it simple to design user interfaces by writing them in a clean, declarative way that's easier to read than traditional code.",
    "Flet": "Write one Python program that runs on Windows, Mac, Linux, phones, and web browsers—perfect if you want to reach multiple platforms without rewriting your code.",
    "Flexx": "Creates desktop applications using web technology and Python, so you can build beautiful, interactive programs with the flexibility of web design.",
    "Gooey": "Transform your simple command-line program into a full graphical application with a single line of code—no GUI experience needed.",
    "kivy": "Build touch-friendly mobile and desktop apps in pure Python that work on phones, tablets, and computers with the same code.",
    "pyglet": "A lightweight toolkit for creating games and multimedia applications with graphics, sound, and animations that work across different operating systems.",
    "PyGObject": "Connect Python to GTK, giving you access to the same graphics tools that power many Linux desktop applications.",
    "PyQt": "Build professional desktop applications for Windows, Mac, and Linux using the same powerful tools that professionals use to create traditional software.",
    "PySimpleGUI": "The easiest way to add buttons, windows, and menus to your Python script—works with multiple graphics frameworks without you having to learn them all.",
    "pywebview": "Wrap a web interface around your Python code to create a desktop app that looks modern and uses web technologies like HTML and JavaScript.",
    "Tkinter": "Python's built-in tool for creating simple desktop applications with windows, buttons, and text boxes—easy to learn and comes with Python.",
    "Toga": "Write one Python program that automatically looks native on Windows, Mac, iOS, and Android—matching each platform's design style perfectly.",
    "urwid": "Build sophisticated text-based user interfaces for the terminal with support for colors, animations, and interactive elements.",
    "wxPython": "Create native-looking desktop applications for Windows, Mac, and Linux that feel like real software rather than a web app.",
    "DearPyGui": "Build fast, beautiful user interfaces with GPU acceleration, perfect when you need top performance or complex visualizations.",
    "graphene": "Easily create modern APIs that let your applications share data efficiently—popular with web developers who want flexible, powerful APIs.",
    "Arcade": "A beginner-friendly library for making 2D games with Python, complete with graphics, sounds, and all the tools you need to bring your game ideas to life.",
    "Cocos2d": "Build 2D games and animated applications with a framework designed to make graphics and interactions feel smooth and responsive.",
    "Harfang3D": "Create 3D games and virtual reality experiences with Python, giving you access to powerful 3D graphics without complex C++ code.",
    "Panda3D": "A professional 3D game engine created by Disney that's free for everyone—build games and 3D applications with industrial-strength tools.",
    "Pygame": "The most popular Python tool for making 2D games—provides everything you need: graphics, sound, input, and collision detection.",
    "PyOgre": "Access professional 3D rendering technology through Python for games, simulations, and any application that needs impressive 3D visuals.",
    "PyOpenGL": "Direct access to low-level graphics programming for creating custom 3D effects and high-performance visualizations.",
    "PySDL2": "Use the powerful SDL game development library from Python to create games and multimedia applications across multiple platforms.",
    "RenPy": "Specialized tool for creating visual novels and interactive story games where players make choices that affect the narrative.",
    "django-countries": "Quickly add country selection fields to your Django website, automatically handling all country names and codes for you.",
    "geodjango": "Add location-based features to your website, like maps and location searches, with built-in geographic database support.",
    "geojson": "Work with map data in Python by reading and writing GeoJSON—a standard format for sharing geographic information.",
    "geopy": "Convert addresses to coordinates and coordinates to addresses, or calculate distances between locations—all with a few lines of code.",
    "beautifulsoup": "Extract data from websites by parsing HTML, making it easy to scrape information and automate web tasks without complex code.",
    "bleach": "Clean up user-submitted HTML to remove dangerous code while keeping the safe, formatted content—essential for websites that accept user input.",
    "cssutils": "Parse, validate, and manipulate CSS stylesheets in Python, useful for analyzing web styling or programmatically generating styles.",
    "html5lib": "Parse and fix broken HTML the way web browsers do, making it reliable for extracting data from messy or malformed web pages.",
    "lxml": "Lightning-fast library for reading and manipulating HTML and XML documents—much faster than alternatives when dealing with large files.",
    "markupsafe": "Safely handle text that contains special characters and HTML, preventing security vulnerabilities when displaying user input on websites.",
    "pyquery": "Query and manipulate HTML documents using jQuery-style syntax, making web scraping feel familiar if you know JavaScript.",
    "untangle": "Convert XML files into simple Python objects, making it natural to access and work with structured data without parsing complexity.",

    # Batch 4
    "WeasyPrint": "Convert HTML and CSS documents into beautiful PDF files programmatically, perfect for generating invoices, reports, or any document from web content.",
    "xmldataset": "Easily read and parse XML files without complicated code, making it simple to extract data from XML documents.",
    "xmltodict": "Transform XML files into Python dictionaries so you can work with XML data just like you would with JSON.",
    "httpx": "A modern tool for sending HTTP requests to websites and APIs, with better features than older alternatives.",
    "requests": "The easiest way to download web pages and interact with web APIs in Python, designed to be simple and intuitive.",
    "treq": "An HTTP library that works like requests but is built for asynchronous operations when you need faster, non-blocking web requests.",
    "urllib3": "A powerful HTTP library that handles connection pooling efficiently and safely manages multiple web requests at once.",
    "keyboard": "Monitor and control keyboard inputs on your computer, allowing you to detect key presses or simulate typing programmatically.",
    "mouse": "Track and control mouse movements and clicks on your computer, useful for automation or testing applications.",
    "pynput": "Control and monitor your keyboard and mouse inputs, perfect for building automated scripts or testing software.",
    "scapy": "Create, send, and analyze network packets to understand network traffic, test network security, or develop network tools.",
    "pillow": "Edit and create images with Python, letting you resize, crop, rotate, and modify photos and graphics easily.",
    "python-barcode": "Generate barcode images that you can use in your applications without needing extra software dependencies.",
    "pymatting": "Remove backgrounds from images or extract subjects with professional-quality transparency effects.",
    "python-qrcode": "Create QR codes that people can scan with their phones, useful for sharing links or information in a compact format.",
    "pywal": "Automatically extract color palettes from images to create matching color schemes for your applications or designs.",
    "pyvips": "Process images extremely fast and efficiently, even when working with very large images that would use too much memory otherwise.",
    "quads": "Turn photos into abstract art by breaking them down into colored squares, creating stylized digital paintings.",
    "scikit-image": "A comprehensive library for analyzing and processing images scientifically, useful for computer vision and image analysis projects.",
    "thumbor": "Automatically resize, crop, and flip images on demand, perfect for serving optimized images to websites and apps.",
    "wand": "Use ImageMagick's powerful image processing capabilities from Python, giving you professional-grade image editing features.",
    "cpython": "The standard Python interpreter written in C, which powers most Python installations and is what you're using when you run Python normally.",
    "cython": "Speed up your Python code dramatically by converting it to C, making performance-critical applications much faster.",
    "clpython": "Run Python code using Common Lisp as the foundation instead of C, for specialized programming environments.",
    "ironpython": "Run Python code on the Microsoft .NET platform, letting you use Python with Windows-specific libraries and tools.",
    "micropython": "Run Python on tiny devices like microcontrollers and single-board computers with minimal memory.",
    "numba": "Make math-heavy and scientific Python code run much faster by automatically compiling it to machine code.",
    "peachpy": "Write ultra-optimized low-level processor instructions directly from Python for maximum performance in specialized cases.",
    "pypy": "An alternative Python interpreter that runs code much faster than standard Python through clever optimization techniques.",
    "pyston": "A faster version of Python that uses just-in-time compilation to speed up your programs automatically.",
    "bpython": "A friendlier interactive Python shell with color-coding, auto-completion, and better navigation than the standard interpreter.",
    "Jupyter Notebook (IPython)": "Create interactive notebooks that mix code, documentation, and visualizations in your browser, perfect for learning, exploring data, and sharing results.",
    "ptpython": "An advanced Python shell with syntax highlighting, better auto-completion, and a cleaner interface for interactive coding.",
    "Babel": "Support multiple languages and regions in your application by handling translations, date formatting, and localization automatically.",
    "PyICU": "Handle international text properly by supporting multiple languages, character sets, and cultural conventions in your Python programs.",
    "Airflow": "Design, schedule, and monitor complex workflows and data pipelines visually, perfect for automating recurring data tasks.",
    "APScheduler": "Schedule Python functions to run at specific times or intervals, like a task scheduler built right into your code.",
    "django-schedule": "Add calendar scheduling features to Django websites, letting users book appointments or manage events.",
    "doit": "Automate and manage tasks in your projects, similar to build tools like Make but easier to use with Python.",
    "gunnery": "Run tasks across multiple machines with a web interface to manage and monitor them from one place.",
    "Joblib": "Speed up your code by running parts of it in parallel on multiple cores, great for data processing and machine learning.",
    "Plan": "Write scheduled tasks in Python instead of cryptic crontab syntax, making scheduling jobs on servers much easier.",
    "Prefect": "Build reliable data pipelines that automatically handle failures and send alerts, making data processing production-ready.",
    "schedule": "Schedule Python functions to run at specific times using simple, readable code that anyone can understand.",
    "Spiff": "Create complex workflows and state machines that manage how tasks flow through your application.",
    "TaskFlow": "Execute tasks reliably with automatic error handling and recovery, ensuring your processes complete successfully even when something goes wrong.",
    "logbook": "Record what your program is doing in an easier and more flexible way than Python's standard logging system.",
    "logging": "Track what your program is doing by recording messages at different importance levels, essential for understanding how your code behaves.",
    "loguru": "Make logging in Python enjoyable with colorful output, easy configuration, and automatic file rotation for a better development experience.",
    "sentry-python": "Automatically catch and report errors that happen in production, letting your team know immediately when something breaks.",

    # Batch 5
    "structlog": "Makes it easy to keep organized records of what your Python program is doing by logging information in a structured, readable format.",
    "gym": "A practice environment where you can teach a computer program to learn and make decisions, like training a bot to play games.",
    "H2O": "A machine learning platform that helps you build predictive models quickly, even with very large datasets.",
    "Metrics": "Provides tools to measure how accurate your machine learning models are so you know if they're working well.",
    "NuPIC": "A framework for building intelligent programs that can learn patterns from data and make predictions over time.",
    "scikit-learn": "The most beginner-friendly Python tool for machine learning, with simple functions to train models and make predictions.",
    "Spark ML": "Apache Spark's machine learning library that lets you build and train models on massive amounts of data across multiple computers.",
    "vowpal_porpoise": "A lightweight Python tool for fast machine learning on huge datasets that don't fit in memory.",
    "xgboost": "A powerful and fast machine learning algorithm that works especially well for competitions and real-world prediction problems.",
    "MindsDB": "An AI layer for databases that makes it easy to add machine learning predictions directly to your data without complex setup.",
    "Python(x,y)": "A ready-to-use Python package that comes pre-installed with popular scientific tools for data analysis and visualization.",
    "pythonlibs": "A collection of pre-built Python libraries for Windows that are hard to install normally, ready to download and use.",
    "PythonNet": "Lets you use Python code alongside .NET libraries and programs on Windows, bridging two different programming worlds.",
    "PyWin32": "Gives Python access to Windows-specific features like the file system, registry, and other system tools.",
    "WinPython": "A portable version of Python designed for Windows that includes scientific tools and doesn't require installation.",
    "blinker": "A simple messaging system that lets different parts of your Python program send signals to each other when events happen.",
    "boltons": "A collection of handy utility functions that make common Python tasks easier and faster to code.",
    "itsdangerous": "Helps you safely pass data through untrusted environments (like user browsers) by digitally signing it so you know it hasn't been changed.",
    "magenta": "A Google tool that uses AI to automatically generate original music and art from simple ideas or patterns.",
    "pluginbase": "Makes it easy to build Python programs that can be extended with plugins, letting users add new features without modifying the main code.",
    "tryton": "A complete business software framework for building accounting, inventory, and sales applications quickly.",
    "mininet": "A tool that creates a pretend computer network on your machine so you can test network software without real hardware.",
    "napalm": "Simplifies managing network equipment from different vendors by giving you a single, simple way to control them all.",
    "pox": "A Python framework for writing software-defined network controllers that manage how network traffic flows.",
    "django-activity-stream": "Automatically tracks and records user actions on your website (likes, comments, follows) so you can show activity feeds.",
    "Stream Framework": "Builds fast, scalable news feeds and notifications for websites using fast databases in the background.",
    "pip": "The standard tool for installing Python libraries from the internet so you can use them in your projects.",
    "conda": "A package manager that installs not just Python libraries but also complex scientific tools with all their dependencies.",
    "poetry": "A modern tool that handles installing libraries and managing project dependencies while keeping everything organized and reproducible.",
    "uv": "An extremely fast, modern package manager built in Rust that installs Python libraries and manages projects lightning quick.",
    "bandersnatch": "A tool for creating a local copy of the entire Python library repository so you can access packages without internet.",
    "devpi": "A private Python package server that lets you store, test, and release your own libraries internally before sharing them.",
    "localshop": "A simple local Python package server that caches libraries and lets you host your own private packages.",
    "warehouse": "The modern software behind the official Python Package Repository (PyPI) where all Python libraries are hosted.",
    "fsociety": "A framework with tools for security testing and ethical hacking to find vulnerabilities in systems.",
    "setoolkit": "A toolkit for security professionals to test how vulnerable organizations are to social engineering attacks.",
    "sqlmap": "An automated security testing tool that checks if websites are vulnerable to SQL injection attacks.",
    "django-guardian": "Adds fine-grained permission control to Django websites so you can control who can access specific database records.",
    "django-rules": "A lightweight permission system for Django that lets you define access rules without storing extra database records.",
    "delegator.py": "Makes running system commands from Python simpler and cleaner, letting your code control other programs easily.",
    "sarge": "A simpler, more powerful way to run other programs from your Python code with better control over input and output.",
    "sh": "Lets you call system commands in Python as if they were regular Python functions, making scripts easier to write.",
    "annoy": "A fast, memory-efficient tool for finding similar items in your data, useful for search and recommendation systems.",
    "fastFM": "A fast library for building recommendation systems that predict user preferences based on patterns in data.",
    "implicit": "A high-speed recommendation engine that learns from user behavior (clicks, purchases) to suggest relevant products.",
    "libffm": "A specialized library for building predictive models that consider relationships between different features in your data.",
    "lightfm": "An easy-to-use Python library for building recommendation systems that suggest items users might like.",
    "spotlight": "Uses deep learning and PyTorch to build advanced recommendation systems that predict what items users will prefer.",
    "Surprise": "A beginner-friendly toolkit for building and testing recommendation systems that suggest movies, products, or content.",
    "tensorrec": "A framework built on TensorFlow for creating recommendation systems that predict what users will enjoy.",

    # Batch 6
    "Bicycle Repair Man": "A refactoring tool that helps you automatically rename, reorganize, and improve the structure of your Python code without breaking it.",
    "Bowler": "A modern tool that safely refactors your Python code by automatically finding and fixing code patterns across your entire project.",
    "Rope": "A Python refactoring library that helps you rename variables, extract functions, and reorganize code programmatically.",
    "PythonRobotics": "A collection of robot movement and navigation algorithms with visual demonstrations, perfect for learning how robots plan paths and avoid obstacles.",
    "rospy": "A library for writing Python programs that control and communicate with robots using the Robot Operating System (ROS).",
    "zeroRPC": "A tool for calling Python functions across different computers or programs over the network with minimal setup.",
    "astropy": "A toolbox for astronomers and space scientists to analyze data from telescopes and study stars and galaxies.",
    "bcbio-nextgen": "A automated pipeline for analyzing DNA sequencing data from genetic research projects quickly and reliably.",
    "bccb": "A collection of useful tools for biological research, including code for analyzing genetic data and protein sequences.",
    "Biopython": "A toolkit for biologists to work with DNA sequences, proteins, and other biological data in Python.",
    "cclib": "A tool that reads and interprets data from chemistry software, making it easy to analyze molecular simulation results.",
    "Colour": "A library for working with colors and light in scientific applications, including color conversion and visual rendering calculations.",
    "Karate Club": "A machine learning toolkit for finding patterns and communities in network data, like social media connections or relationships.",
    "NetworkX": "A powerful library for creating, analyzing, and visualizing networks like social networks, computer networks, or biological systems.",
    "NIPY": "A collection of tools for analyzing brain imaging data from MRI and fMRI scans used in neuroscience research.",
    "NumPy": "The foundation of scientific computing in Python, providing fast arrays and math operations that make data analysis practical.",
    "ObsPy": "A toolbox for seismologists to download, process, and analyze earthquake and seismic wave data from monitoring networks.",
    "Open Babel": "A chemistry tool that converts between different molecular data formats, making it easy to work with chemical structures.",
    "PyDy": "A library for modeling and simulating systems that move and change over time, like robots, vehicles, or mechanical structures.",
    "PyMC": "A tool for solving uncertainty problems by using statistical sampling to explore possible solutions and their probabilities.",
    "QuTiP": "A toolkit for quantum mechanics calculations, used to simulate and analyze quantum systems and quantum computing.",
    "RDKit": "A chemistry library that helps you work with molecular structures, predict chemical properties, and apply machine learning to drug discovery.",
    "SciPy": "A comprehensive science toolkit that extends NumPy with algorithms for optimization, statistics, signal processing, and more.",
    "SimPy": "A simulation library for modeling real-world processes like traffic flow, queues, or manufacturing systems to predict outcomes.",
    "statsmodels": "A library for building and testing statistical models and analyzing economic and financial data.",
    "SymPy": "A tool for symbolic mathematics that can solve equations, simplify expressions, and perform calculus like a math textbook.",
    "Zipline": "A framework for testing and backtesting stock trading strategies using historical market data.",
    "django-haystack": "A search plugin for Django websites that lets you add powerful search functionality to your web applications.",
    "elasticsearch-dsl-py": "An easy-to-use tool for building search applications that can handle billions of documents and find results in milliseconds.",
    "elasticsearch-py": "The official low-level client for connecting Python code to Elasticsearch search engines for customized search behavior.",
    "pysolr": "A simple Python connector for Apache Solr that lets you index and search large amounts of text data.",
    "whoosh": "A pure Python search engine library that you can embed directly in your Python programs without external dependencies.",
    "marshmallow": "A tool for converting between complex Python objects and simple formats like JSON, useful for APIs and data validation.",
    "pysimdjson": "An extremely fast JSON parser that uses modern computer processor tricks to read JSON files at lightning speeds.",
    "python-rapidjson": "A high-performance JSON reader and writer that's much faster than Python's built-in JSON module.",
    "toonify": "A compact data format that uses fewer tokens than JSON, perfect for reducing costs when working with AI language models.",
    "ultrajson": "An ultra-fast JSON encoder and decoder written in C that dramatically speeds up processing large JSON data.",
    "python-lambda": "A toolkit that makes it easy to write and deploy Python code to AWS Lambda for running serverless functions.",
    "Zappa": "A deployment tool that lets you host Django and other Python web applications on AWS Lambda without managing servers.",
    "xonsh": "A shell that combines Python programming language with Unix commands, giving you the power of both in one place.",
    "lektor": "A simple content management system and blog platform that generates static websites from easy-to-edit content files.",
    "mkdocs": "A documentation generator that turns Markdown files into beautiful, professional-looking websites automatically.",
    "makesite": "A tiny, straightforward static site generator that creates websites from files without complex configuration or magic.",
    "nikola": "A flexible static website and blog generator that supports multiple content formats and powerful customization.",
    "pelican": "A static blog generator that converts Markdown and other text formats into a complete, ready-to-deploy website.",
    "django-taggit": "A simple plugin for Django that adds tagging capability to your website, letting you organize content with labels.",
    "celery": "A task scheduler that lets you run Python code in the background and across multiple computers to handle long-running jobs.",
    "dramatiq": "A lightweight task queue that processes background jobs reliably, simpler to set up than more complex alternatives.",
    "huey": "A small task queue system for running background jobs in Python with minimal configuration and overhead.",
    "mrq": "A distributed task queue that uses Redis to coordinate Python workers across multiple computers for processing jobs at scale.",

    # Batch 7
    "rq": "A simple tool for managing background jobs in Python, letting you run tasks without blocking your main application.",
    "Genshi": "A templating tool that generates web pages by combining your data with HTML templates, keeping code and design separate.",
    "Jinja2": "A powerful and easy-to-use templating engine for creating dynamic web pages by inserting data into HTML templates.",
    "Mako": "A lightweight, fast templating library for Python that quickly converts your data into formatted text or web pages.",
    "apache-libcloud": "One unified library to interact with different cloud providers like Amazon, Google Cloud, and Microsoft Azure from a single codebase.",
    "boto3": "The official Python library for interacting with Amazon Web Services, letting you manage AWS resources programmatically.",
    "django-wordpress": "Bridges Django and WordPress, letting you use WordPress content and functionality within your Django web application.",
    "facebook-sdk": "An official tool that lets your Python app interact with Facebook's features, like posting, reading user data, or managing ads.",
    "google-api-python-client": "Access Google's services like Gmail, Drive, and YouTube directly from Python code without using a web browser.",
    "gspread": "Read and write to Google Sheets directly from Python, treating spreadsheets like a simple database.",
    "twython": "A Python library that lets your app interact with Twitter's API to read tweets, post content, and manage followers.",
    "furl": "Makes working with URLs simple by providing an easy way to parse, build, and modify web addresses in Python.",
    "purl": "A clean, simple tool for breaking down and working with URLs in your Python code without messy string manipulation.",
    "pyshorteners": "Converts long URLs into short, shareable links using services like Bitly or TinyURL from your Python code.",
    "webargs": "Automatically extracts and validates data from web requests in your Flask or Django app, saving you from manual parsing.",
    "moviepy": "Create, edit, and combine videos and animated GIFs using Python code instead of video editing software.",
    "scikit-video": "A video processing library that works with Python's scientific computing tools for analyzing and manipulating video files.",
    "vidgear": "A powerful, fast video processing framework for Python that handles multiple videos simultaneously without slowing down.",
    "django-compressor": "Automatically combines and compresses your CSS and JavaScript files on your Django website to make it load faster.",
    "django-pipeline": "Manages and optimizes static files (images, CSS, JavaScript) in your Django app for better website performance.",
    "django-storages": "Extends Django to store files on cloud services like S3 or Google Cloud Storage instead of your server's disk.",
    "fanstatic": "Bundles your JavaScript and CSS files as reusable Python packages with automatic caching and delivery.",
    "fileconveyor": "Automatically watches your files and syncs them to content delivery networks or cloud storage like S3 when they change.",
    "flask-assets": "Optimizes and combines CSS and JavaScript files in Flask apps to improve website loading speed.",
    "webassets": "Bundles and optimizes static website files while managing unique URLs to prevent browsers from using old cached versions.",
    "html2text": "Converts HTML web pages into readable Markdown format, useful for extracting content from websites.",
    "lassie": "Pulls metadata and content from web pages automatically, extracting titles, images, and descriptions.",
    "micawber": "Extracts embedded media and rich content from URLs, like previews from YouTube videos or Twitter posts.",
    "newspaper": "Extracts news articles and content from websites, cleaning up the text and organizing it into readable formats.",
    "python-readability": "Removes clutter from web pages and extracts the main article content, similar to browser reader modes.",
    "requests-html": "A beginner-friendly library for downloading and parsing HTML from websites with clean, readable code.",
    "sumy": "Automatically summarizes long documents or web pages into shorter versions that capture the main ideas.",
    "textract": "Pulls text out of any document type like Word files, PDFs, and PowerPoint presentations in one simple command.",
    "toapi": "Turns any website into an API, letting you access website content as structured data without official API support.",
    "feedparser": "Reads blog feeds and news feeds from websites, parsing RSS and Atom content into usable Python data.",
    "grab": "A complete framework for scraping websites and collecting data at scale with built-in tools for handling complex sites.",
    "mechanicalsoup": "Automates interactions with websites like filling forms and clicking buttons, useful for testing or data collection.",
    "scrapy": "A professional framework for building web scrapers that can efficiently collect data from large websites.",
    "autobahn-python": "Enables real-time two-way communication between web browsers and Python servers using WebSocket connections.",
    "channels": "Adds real-time features like live notifications and chat to Django apps by supporting WebSocket connections.",
    "websockets": "A simple, reliable library for creating real-time connections between Python apps and web browsers or other clients.",
    "gunicorn": "A web server that runs your Python web app and handles multiple requests from users at the same time.",
    "uwsgi": "A powerful, high-performance web server for running Python web applications in production environments.",
    "waitress": "A simple web server for running Python web apps, especially popular with the Pyramid framework.",
    "werkzeug": "A utility library that powers Flask and provides tools for handling web requests, cookies, and file uploads."
}

# Journalism/media relevant libraries
journalism_relevant = [
    "streamlit",  # Data dashboards for newsroom
    "pandas",  # Data journalism / analysis
    "datasette",  # Publishing databases as websites
    "altair", "bokeh", "matplotlib", "seaborn",  # Data visualization
    "cartopy",  # Maps for geographic reporting
    "diagrams",  # Explaining systems/infrastructure
    "beautifulsoup", "scrapy", "newspaper",  # Web scraping for research
    "requests", "httpx",  # Accessing APIs and web data
    "pillow", "opencv",  # Image processing
    "pytesseract", "easyocr",  # OCR for documents
    "moviepy", "vidgear",  # Video processing
    "youtube-dl",  # Downloading source material
    "WeasyPrint",  # PDF generation for reports
    "feedparser",  # Monitoring RSS feeds
    "python-readability",  # Article extraction
    "textract",  # Document text extraction
    "sumy",  # Automatic summarization
    "gspread",  # Google Sheets integration
    "wagtail",  # CMS for news sites
    "pelican", "mkdocs",  # Publishing platforms
    "flask-admin", "django-grappelli",  # Admin interfaces
    "geodjango", "geopy",  # Location-based reporting
    "django-taggit",  # Content organization
    "python-lambda", "Zappa",  # Serverless news tools
    "schedule", "APScheduler",  # Scheduled data collection
]

def main():
    # Read current libraries.js
    with open('../assets/data/libraries.js', 'r') as f:
        content = f.read()

    # Find all library objects
    pattern = r'\{\s*n:\s*"([^"]+)",\s*c:\s*"([^"]+)",\s*d:\s*"([^"]+)",\s*l:\s*"([^"]+)"\s*\}'

    def replace_description(match):
        name = match.group(1)
        category = match.group(2)
        old_desc = match.group(3)
        link = match.group(4)

        # Get enhanced description if available
        new_desc = enhanced_descriptions.get(name, old_desc)

        # Add journalism tag if relevant
        journalism_tag = ""
        if name in journalism_relevant:
            journalism_tag = ' [JOURNALISM]'

        return f'{{ n: "{name}", c: "{category}", d: "{new_desc}{journalism_tag}", l: "{link}" }}'

    # Replace all descriptions
    new_content = re.sub(pattern, replace_description, content)

    # Write updated content
    with open('../assets/data/libraries.js', 'w') as f:
        f.write(new_content)

    print(f"✓ Updated {len(enhanced_descriptions)} library descriptions")
    print(f"✓ Tagged {len(journalism_relevant)} libraries as journalism-relevant")
    print("\nEnhanced descriptions merged into libraries.js!")

if __name__ == '__main__':
    main()
