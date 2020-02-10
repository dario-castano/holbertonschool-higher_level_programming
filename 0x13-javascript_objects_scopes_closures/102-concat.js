#!/usr/bin/node

const { exec } = require('child_process');

const argv = process.argv.slice(2)
const afile = argv[0];
const bfile = argv[1];
const outfile = argv[2];

const cmd = `cat ${afile} ${bfile} > ${outfile}`

exec(cmd)
