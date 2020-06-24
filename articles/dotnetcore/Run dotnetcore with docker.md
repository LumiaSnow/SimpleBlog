# Frequently Used Docker Commands

December 18, 2019 by Meepo, Docker

---

## 1.Dockerfile

Dockerfile放在项目根目录

```Dockerfile
FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build
WORKDIR /app

# copy csproj and restore as distinct layers
COPY ./*.csproj ./
RUN dotnet restore

# copy everything else and build app
COPY ./. ./
WORKDIR /app
RUN dotnet publish -c Release -o out


FROM mcr.microsoft.com/dotnet/core/aspnet:3.1 AS runtime
WORKDIR /app
COPY --from=build /app/out ./
ENTRYPOINT ["dotnet", "ToshibaCloud.ThirdPartyServer.dll"]
```

## 2 Build Docker Image

清理项目目录, 把bin和obj文件夹清理掉

```bash
dotnet clean
```

将项目文件复制到dockers环境下

Build Docker Image

```bash
docker build -t toshibacloud.thirdpartyserver .
```

## 3 Run

```bash
docker run --name ThirdPartyServer7783 -d -p 7783:7783 -v /root/ToshibaCloud/ToshibaCloud.ThirdPartyServer/Data:/app/Data -v /root/ToshibaCloud/ToshibaCloud.ThirdPartyServer/logs:/app/logs toshibacloud.thirdpartyserver
```
