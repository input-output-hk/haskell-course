#!/bin/bash

pushd "$(dirname "${BASH_SOURCE[0]}")"

[[ -n ${1} ]] &&
	tagArgs=" -t ${1} "

docker build --build-arg NB_USER=$(whoami) --build-arg NB_UID=$(id -u) ${tagArgs} .

popd
