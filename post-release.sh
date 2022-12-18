#!/bin/sh

VERSION=$1
CRATES="data linalg core nnef pulse-opl pulse hir tensorflow onnx-opl onnx kaldi libcli cli ffi"

if [ `uname` = "Darwin" ]
then
    SED=gsed
else
    SED=sed
fi

if [ -z "$VERSION" ]
then
    echo "Usage: $0 <version>" 
    exit 1
fi

for member in $(grep '^ *"' Cargo.toml | tr -d '",')
do
    f=$member/Cargo.toml
    back=$(echo $member | sed 's/[^\/]\+/../g')
    tomato set package.version $VERSION $f
    for dep in $CRATES
    do
        if tomato get dependencies.tract-$dep.version $f | grep -F .
        then
            tomato set dependencies.tract-$dep.version $VERSION $f
            tomato set dependencies.tract-$dep.path $back/$dep $f
        fi
    done
done

git commit . -m "post-release $VERSION"
