from fabric.api import local
from fabric.api import task

ELK = 'docker-compose -f docker-compose/elk.yml up'


@task
def elk():
    local(ELK)
