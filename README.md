<p align="center"><img width="25%" src="https://github.com/FaceONNX/FaceONNX/raw/main/docs/FaceONNX.png" /></p>
<p align="center"> Face recognition and analytics library based on deep neural networks and <b>ONNX</b> runtime </p>  
<p align="center"><i> A vision of what might lie across the universe... </i></p>  

# FaceONNX
**FaceONNX** is a face recognition and analytics library based on [ONNX](https://onnx.ai/) runtime. It containts ready-made deep neural networks for face
* detection and landmarks extraction,
* gender and age classification,
* emotion and beauty classification,
* embeddings comparison and etc.  

# Version
You can build **FaceONNX** from sources or install to your own project using nuget package manager.
| Assembly | Specification | OS | Platform | Package | Algebra |
|-------------|:-------------:|:-------------:|:--------------:|:--------------:|:--------------:|
| [FaceONNX](https://github.com/FaceONNX/FaceONNX/tree/main/netstandard/FaceONNX) | .NET Standard 2.0 | Cross-platform | CPU | [NuGet](https://www.nuget.org/packages/FaceONNX/) | [UMapx](https://github.com/asiryan/UMapx) |
| [FaceONNX.Addons](https://github.com/FaceONNX/FaceONNX/tree/main/netstandard/FaceONNX.Addons) | .NET Standard 2.0 | Cross-platform | CPU | [NuGet](https://www.nuget.org/packages/FaceONNX.Addons/) | [UMapx](https://github.com/asiryan/UMapx) |
| [FaceONNX.Gpu](https://github.com/FaceONNX/FaceONNX/tree/main/netstandard/FaceONNX.Gpu) | .NET Standard 2.0 | Cross-platform | GPU | [NuGet](https://www.nuget.org/packages/FaceONNX.Gpu/) | [UMapx](https://github.com/asiryan/UMapx) |
| [FaceONNX.Addons.Gpu](https://github.com/FaceONNX/FaceONNX/tree/main/netstandard/FaceONNX.Addons.Gpu) | .NET Standard 2.0 | Cross-platform | GPU | [NuGet](https://www.nuget.org/packages/FaceONNX.Addons.Gpu/) | [UMapx](https://github.com/asiryan/UMapx) |

# Installation
C# interface  
```c#
using FaceONNX;
```
To get started with **FaceONNX**, it is recommended to look at the folder with [examples](https://github.com/FaceONNX/FaceONNX/tree/main/netstandard/Examples).  

# References 
[ONNX models](https://github.com/FaceONNX/FaceONNX.Models)  

# License
**FaceONNX** is released under the [MIT](https://github.com/FaceONNX/FaceONNX/blob/main/LICENSE) license.
