# Insecure Task Challenge

## How to install
### Get the source code
1. Download and install VS Code (https://code.visualstudio.com/) or use another Platform (this tutorial uses VS Code)
2. Open VS Code, on the left site go to Source Control
3. Click on "Clone Repository" and paste https://github.com/annfii/Insecure_Task_App.git
4. Select a folder where to save the repository, then open the project
5. Trust the authors of the project

### Run the code
#### Using Python
1. Download and install Python (https://www.python.org/downloads/)
2. In VS Code on the top select Terminal -> New Terminal
3. Run the command "pip3 install -r requirements.txt"
4. Run the command ".\run.sh"
5. Open your Browser and navigate to http://127.0.0.1:5000

#### Using Docker (Recommended)
1. Make sure to have Docker installed 
   -   For Windows: \
       a. Have WSL installed (https://learn.microsoft.com/en-us/windows/wsl/install) \
       b. Have Docker Desktop installed (https://docs.docker.com/desktop/wsl/)
   - For Mac: \
       a. Have Docker Desktop installed (https://docs.docker.com/desktop/install/mac-install/)
2. Navigate into the cloned repository and there into the directory: "Insecure_Task_App"
3. Execute the command to pull the python environment for your container image: "docker pull python:3.10" (without the quotation marks)
4. Build the container image: "docker build -t vuln-tasks-app ." (without the quotation marks; you need to be in the directory Insecure_Task_App; you need the dot at the end of the command!!)
5. Run the container: "docker run -it -d -p 5001:5000 vuln-tasks-app"
6. Open your browser and navigate to http://127.0.0.1:5001


#### Note: You do not need any external tools, you can solve all tasks with the browser developer tool (F12) and browser console (Firefox). 
#### Evaluation: 10 Points (Highest Grade) + 3 Extra Points
#### Optional tasks do not count toward the final grade.


#### ( ﾉ ﾟｰﾟ)ﾉ GOOD LUCK AND HAVE FUN!＼(ﾟｰﾟ＼)


## Challenge Start
You are part of a pentesting team and your customer is about to release the new Task
Manager application. However, before they release it, they need to make sure that
there are no security problems in the application. Therefore, it is your job to find
vulnerabilities by performing a whitebox pentest, which means that you are provided
with the source code of the application. However, the client wants you to demonstrate
and advise on how a vulnerability could be exploited and how to mitigate it. 
Let’s start with the results as the vulnerability scanner has already found three vulnerabilities. 
Keep in mind, however, that the scanner will certainly not have found all the vulnerabilities.

Because it is a highly secure vulnerability scanner, it has encrypted its findings.
Are you able to decrypt the found tasks? **(1 Point)**

### General tips for all challenges
1. Start by examining the project structure carefully
2. Look for any unusual or hidden files/folders
3. The challenges have been encrypted with a public-key cryptosystem
4. The hints are encoded
5. Many vulnerabilities are commonly known so you can find many resources for further help


### Challenge One (3 Points)
DUgQ8IPKONloFDGwAEP4EjG5dWicXjZLd8Xe858IglP/qDBwcpoWna0SFfcyZn3pdM502dqWI78v6rd2kms7M9yg4WklGBuF4+vQKX1frvGhKO9UP3wEsCvdvhfr1+Mn4WyspVHnPaVYLu9+fQrz907Qes59CfleMfc0NpOy+8BSH/9oH2VdhiDZ48HBxTbNsy6ENNUl9uLzCdPosQ7JI6MmNxxCy9Hqw9Fc9LhanJ5OXrDWUmbv/RPoaPwRz06CPy0bFlff+xro9dt1MRZ0KSHgG8nCdAG0UqBesS2I27hEznBqXmaMkBTskwnbcp8FQ7H4mTaSX7DGJNRyhtKb+fsjg5EkrG3k0hCdhwPwC8ZwTsBLItu1U+OxQIoezrzsrcUdGcE+7UoRawoIgZhb3rXxdt+00feDnWeRtOPTBlYI4qAKHJe1ETy4g24ULF10HirCumNKd7dWmj8yTpZRSR0w4dwlDbQlaO2UQZqg/AfUACuv1zntExZMztvm9/GhrcKyvjGevdQ5O3Na5WkLE8EF4hHs9Cqc1+kB6YuLxYhcSteYRtK6Pc4KTlHO3Z+LOGxJRvK/FKigPoutJH3WyxHFPcQDLmtdWr2tcPLyzNOcEuq6T7+Zbt3OvXNdU4YUaSVohxfAQbVhfHsA8jBP5vAYVHnio0iy2A7wLnFQ92E=

**Hints:**
VGlwcyBvbiBDaGFsbGVuZ2UgMToKMS4gTG9vayBhdCB0aGUgY29kZSBpbXBsZW1lbnRlZCBpbiBhcHAucHkKMi4gV2hhdCBoYXBwZW5zIGlmIHlvdSBhZGQgc3BlY2lhbCBTUUwgY2hhcmFjdGVycyB0byB0aGUgbG9naW4gZm9ybT8KMy4gU1FMIHF1ZXJpZXMgYXJlIG9mdGVuIHRlcm1pbmF0ZWQgd2l0aCBzZW1pY29sb25zLiBXaGF0IGlmIHlvdSBjb3VsZCBlbmQgdGhlIHF1ZXJ5IGVhcmx5Pw==



### Challenge Two (3 Points)
omzjl0pn+JEQh1LJy1q92bN/7yVKqlNsus7IWQh+DgvKLo1Vbu7jNPd5HgqaQTMD8Tf6e0sWKNGUx/uHWGGJC73Zk9BPqdAS8odkyaWbhT7PvvaKZQEGrWfX1+Eh9tvAIGqOnR28E7vmi+Qqiy3jBq6sCFKIhDL35jGVRAAAaLrgX+xz8/hehXoBiQG6Mut+rVO6qh6DhtCBXgtZiPiCSY74GH6sVTJnWIqrnVd/WCAbZKABgOwrIpNDkm64XYe6SAM9MSX+bauyr4PmBxDTXZoWyFq8h0uJwOHb6WX/43XDZ8kUDF0Kp13BhUBLWnKKpmVx+pEFvWPub5NuN9xQqoN2DLsHZHxcpdQdFQ6/Z+2Sxn9ut8gq+cO/ToAj98o8IIntUah3aWmsc78jZNf0eygidkQgmicliIQrYUjXHeGuzN1yPX7CY2nmlHUOhuF8MJTA249qGOjfmIqTdxpXM18VaNY1StTRGjqa4R91gp/l8k4sRegVdX1m9Ebi0/iv41rfMp6W5GwLQ7PS3y7wyovqq0/3ICX3SOWGznNhp+9/0r8frPnNU6my9m6Dj5OvUdM/YiPa5f7kSxRI0BaWwtuzs0emyeFnfm4YhJtjBC6anAiMa08FdRA+Y4yUycuzxcQ8hqsxjbi48cLXZQYLQNLu+5B3JDulUwNDVZp8eZc=

**Hints:**
VGlwcyBvbiBDaGFsbGVuZ2UgMjoKMS4gTG9vayBhdCBob3cgaW1hZ2VzIGFyZSBsb2FkZWQgaW4gdGhlIGJsb2cgc2VjdGlvbi4KMi4gQ2hlY2sgdGhlIFVSTCBwYXJhbWV0ZXJzIHdoZW4gdmlld2luZyBibG9nIGltYWdlcy4KMy4gVGhlIGFwcGxpY2F0aW9uIHVzZXMgcmVnZXggdG8gZmlsdGVyICcuLi8nIC0gYnV0IGlzIGl0IGVub3VnaD8KNC4gV2hhdCBpZiB3ZSBjb3VsZCAndHJpY2snIHRoZSByZWdleCB3aGlsZSBrZWVwaW5nIHRoZSBwYXRoIHZhbGlkPw==


### Challenge Three (3 Points) 
SwtoDC3blaEKPArRINlBO0R0AGiXfXPh//ZI4E23xDxh+kRGBzcvskquC11zOnfsOhjaunpcjk+ytDx8g0pV75PRNoiIK28ozp5lcujmtmO5O2tdrOxS/J8tvuDbH3U7Q58G6871GW0jPRVMwYNx/npEJ08G+jlpDw/sB9Uty/u2N98GAg68bAOtXMxmaWumE+WopsrfCe9p9pnOKiBOcIcU9wtXBMX7EG+ywOUsvP8hd6ZXUcsgbirIzWM3anAVSTYmvAAB6HE1FXIrAFlvNbTP4H9RC3jp9MrO7PdwFGPMyKqzY+zUPbDCbZl5r2EQXsNX+U3ZfaDwCL3fyG+hv++BfF8LT4h4TkYr+Bk7RJsY8M4EAEPedRa7WsjlaSpdRFNnL/9TgKX3jVNi8sAu4CWHQ4A8aV+XcWBiAFsp+3lT+QxAnwZbdzhOSH1TlTVP1KcK0EeHoCQ1pcHImEIUx8lMvDyfzzGG9hyqtoz//bsDUq36o9bgfDnVbixI9vvD1PTbGv3mH/x7QsLix7HACyb2aU1ivcHvlLZUJwbMle+m2WbIJ8PCVL3pJTkk5S8nO8CNwhHp4kDGHk5eF71DuW1oIWd1U11vmDmwdxLshChXp0e3f/HT0bj0xC+oViw8bYr8GVjTFNYA2+eHwLWS7hVyH2cympLevlHDjxksNWw=

**Hints:**
VGlwcyBvbiBDaGFsbGVuZ2UgMzoKMS4gSG93IGRvZXMgdGhlIGFwcGxpY2F0aW9uIGtub3cgeW91J3JlIGFuIGFkbWluPwoyLiBJcyBpdCByZWFsbHkgYSBnb29kIGlkZWEgdG8gcmVmZXIgZGlyZWN0bHkgdG8gYSBjb29raWUgdGhhdCBob2xkcyB0aGUgdXNlcidzIElEPwozLiBXaGF0J3Mgc3BlY2lhbCBhYm91dCB1c2VyIElEIDE/

### Bonus Questions (1 extra point for each question solved)
JZ4HNc/hg7EX+myr0Agl9leWlyRwIhchtGenWAKihLLXQrnQjJe4l+jw1NV6iFHsidmZmaImZpvQBYCbNSrgIcAC32+3nwbv+L1/E9tp0IqNGX/45LgkkOxkZ/L5PRvQElYU3jDDo2PfHaX7vyrBVtQMJ5KEnoRd3eaGCDlHKoNt1yb4OegkSdEfjPlMqT0/P3LAQNQD/x4TbBuR4zFSHMuYJEFkOgZwccTlYAhyANK86jSAP3UBvunx/iiswWty4PKjUrKRJ+m4JYb3FZij1AyIvF6eEW54fn3a3kAgSvh92horrDO2Epjw1fJ4DWXaYlYz/MZhHLkeK98YJdf8sHZ80OcMgPyhL3VXdW8bbvmjRFeek+r//tO3KtWJ9fX0cKxdJvlhENgwdXFdmBW1VuoFy7F86rFGzo70VNn/hDy3lW5T5YUgMm4qZgI5VBCScbiTYJJuvn9ju6qkPfwhLjnefwv9cPEW7/Y51qCq6rLaAIeYIyjRRi74tWiNzMlbUHPVm+tgEhD5q+DJ5iiI0Z71KVJ/utVmJadUJ2RsMAgK02A8RJPIKH+2ouPt1x4A7GHgVP2TS+WkhsF7Pwz0NRO8gavIiqOvdqmCvCbA6kPf0H1yiH520Qz2rR0b6KE/niRh7OkQs/4V0DbIjI77HIWWlUXR2DmHdrwumFj+/u8=

