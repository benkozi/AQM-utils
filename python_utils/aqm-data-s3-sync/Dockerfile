FROM continuumio/miniconda3

RUN apt-get update --yes && apt-get install --yes tmux vim less

COPY environment.yml /opt/build/environment.yml
COPY pyproject.toml /opt/build/pyproject.toml
RUN conda env create -f /opt/build/environment.yml

COPY src /opt/build/src
RUN conda run -n aqm-data-s3-sync pip install .

RUN rm -rf /opt/build
