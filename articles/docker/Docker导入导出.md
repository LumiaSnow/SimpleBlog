# Docker镜像和容器的导入导出

December 18, 2019 by Meepo, Docker

---

## 1.镜像导入导出

### 1.1 镜像导出

命令

```bash
docker save [options] images [images...]
```

示例

```bash
docker save -o nginx.tar nginx:latest
docker save > nginx.tar nginx:latest
```

### 1.2 镜像导入

命令

```bash
docker load [options]
```

示例

```bash
docker load -i nginx.tar
docker load < nginx.tar
```

## 2.容器导入导出

### 2.1 容器导出

命令

```bash
docker export [options] container
```

示例

```bash
docker export -o nginx-test.tar nginx-test
```

### 2.2 容器导入

命令

```bash
docker import [options] file|URL|- [REPOSITORY[:TAG]]
```

示例

```bash
docker import nginx-test.tar nginx:imp
```
