#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: CommandLineTool
baseCommand: python3
inputs:
  example_file:
    type: File?
    inputBinding:
      prefix: --file=
      separate: false
      position: 4

outputs: []
