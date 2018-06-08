```txt

work with docker and python (also apply for non-compiled language)

    you cam use virtualenv and install dependencies to help ide hint
    but not run code on docker host. For a new dependency update requirements.txt
    and rebuild the image

    .dockerignore are like gitignore, if you add rule *.txt need to add !requirements.txt 
    so docker will complain that file does not exists if you try to use it
    
    install requirements.txt first to work with cache
        COPY requirements.txt /app/
        RUN pip install -r requirements.txt
    
    build image
        docker build -t myipy:1 .
    
    list files at image
        docker run --rm myipy:1 sh -c 'ls'
    
    pass environment variables
        docker run --rm -e DEV=True myipy:1 sh -c 'python main.py'
    
    pass args to python program
        docker run --rm -e DEV=True myipy:1 sh -c 'python main.py g'
    
    map host code with container volume to run container to see simple changes without build entire image
    this can be trick since .dockerignore does not apply here so map just code
        docker run --rm -v "$(pwd)/app":/app/app myipy:1 sh -c 'python main.py'

```
