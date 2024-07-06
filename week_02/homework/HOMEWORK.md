# Homework 02

## Question 01

Run ollama docker image 

```bash
docker run -it \
    --rm \
    -v ollama:/root/.ollama \
    -p 11434:11434 \
    --name ollama \
    ollama/ollama
```

Enter into running ollama container
```bash
docker exec -it ollama bash
```

Print version
```bash
root@5a5fe50d7f66:/# ollama -v
```

Output
```bash
root@5a5fe50d7f66:/# ollama version is 0.1.48
```

### Question 02

Pull gemma:2b

```bash
root@5a5fe50d7f66:/# ollama pull gemma:2b
```

Mata data of gemma:2b

```bash
root@5a5fe50d7f66:/# cat /root/.ollama/models/manifests/registry.ollama.ai/library/gemma
/2b
```

```bash
{"schemaVersion":2,"mediaType":"application/vnd.docker.distribution.manifest.v2+json","config":{"mediaType":"application/vnd.docker.container.image.v1+json","digest":"sha256:887433b89a901c156f7e6944442f3c9e57f3c55d6ed52042cbb7303aea994290","size":483},"layers":[{"mediaType":"application/vnd.ollama.image.model","digest":"sha256:c1864a5eb19305c40519da12cc543519e48a0697ecd30e15d5ac228644957d12","size":1678447520},{"mediaType":"application/vnd.ollama.image.license","digest":"sha256:097a36493f718248845233af1d3fefe7a303f864fae13bc31a3a9704229378ca","size":8433},{"mediaType":"application/vnd.ollama.image.template","digest":"sha256:109037bec39c0becc8221222ae23557559bc594290945a2c4221ab4f303b8871","size":136},{"mediaType":"application/vnd.ollama.image.params","digest":"sha256:22a838ceb7fb22755a3b0ae9b4eadde629d19be1f651f73efb8c6b4e2cd0eea0","size":84}]}
```

### Question 03

Run gemma:2b

```bash
root@5a5fe50d7f66:/# ollama run gemma:2b
```

Prompt

```bash
root@5a5fe50d7f66:/# ollama run gemma:2b
>>> 10 * 10
The answer is 100.
```

### Question 04

Make dir project (week02/homework) dir

```bash
ollama_files
```

Run ollama mounting created folder as a volume

```bash
docker run -it \
    --rm \
    -v ./ollama_files:/root/.ollama \
    -p 11434:11434 \
    --name ollama \
    ollama/ollama
```

Download gemma:2b

```bash
docker exec -it ollama ollama pull gemma:2b 
```

Find disk usage for `ollama/models`

```bash
du -h ollama_files/models 

8.0K    ollama_files/models/manifests/registry.ollama.ai/library/gemma
12K     ollama_files/models/manifests/registry.ollama.ai/library
16K     ollama_files/models/manifests/registry.ollama.ai
20K     ollama_files/models/manifests
1.6G    ollama_files/models/blobs
1.6G    ollama_files/models
```

### Question 05

Copy Weights in Dockerfile

```dockerfile
FROM ollama/ollama

COPY ./ollama_files /root/.ollama
```

### Question 06

Run python script for question 06

```bash
python question06.py
```

Output

```bash
Completion Tokens = 286
```