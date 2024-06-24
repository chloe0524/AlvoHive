#!/bin/bash

for image in logos/*.png
do
    id_image=$(basename "${image}" | awk -F_ '{print $1}')
    file_image=$(echo "${image}" | awk -F_ '{print $2}')
    echo "Traitement id=${id_image} image=${file_image}"
    ./populate_company_logo.py "${image}" ${id_image}
done

