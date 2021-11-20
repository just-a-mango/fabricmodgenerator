#Import everything (and define the color class)
import os, shutil
from datetime import date
from git import Repo
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


#Print title
print(color.GREEN + color.BOLD + '|-----------------------------|\r\n|     Fabric Starter Gen      |    by Just_a_Mango\r\n|-----------------------------|\r\n' + color.END)


#If there is an error, print it 
def error(error):
    print(color.RED + "[ERROR] - " + error + color.END)
    exit()


#Ask questions
mc_version = input(color.BLUE + "Please enter your desired Minecraft version(the only supported options are 1.16, 1.17, and 1.18 and if none is chosen 1.17 will be chosen): ").replace(" ","")
mod_name = input("Please enter your mod's name(ex. MyMod): ").replace(" ","")
maven_group = input("Please enter your maven group(ex. com.mango): ").replace(" ","")
mod_version = input("Please input your mod's first version(ex. 1.0.0): ").replace(" ","")
mod_description = input("Please enter your mod's description: ")
mod_license = input("Please enter your mod's license(ex. MIT): ")
mod_creator = input("Please enter your name(as an author): ")
mod_homepage = input("Please enter your mod's homepage(URL): ")
mod_source = input("Please enter your mod's source location: " + color.END)
license_line = "Copyright © "+str(date.today())+" "+mod_creator


#Define path and clone repository
try:
    path = os.getcwd() + "//" + mod_name + "//"
    os.mkdir(path)
except:
    error("Failed to create the directory for your mod. Please check your mod's name and try again.")
try:
    if mc_version == '1.16':
        Repo.clone_from('https://github.com/FabricMC/fabric-example-mod', path, branch='master')
    elif mc_version == '1.18':
        Repo.clone_from('https://github.com/FabricMC/fabric-example-mod', path, branch='1.18')
    else:
        Repo.clone_from('https://github.com/FabricMC/fabric-example-mod', path, branch='1.17')
        
        
except:
    error("Failed to download the repository from github. If the repository isn't accessible anymore, please check for updates of this project on Github and/or create an issue.")


#Open and modify gradle.properties
try:
    with open(path + 'gradle.properties', 'r') as file:
        filedata = file.read()
except:
    error("Failed to open gradle.properties. Please check if the file exists and try again.")
try:
    filedata = filedata.replace('maven_group = com.example', 'maven_group = ' + maven_group)
    filedata = filedata.replace('fabric-example-mod', mod_name.lower())
    filedata = filedata.replace('1.0.0', mod_version.lower())
except:
    error("Failed to rename references in gradle.properties. Please check the file and try again.")
try:
    with open(path + 'gradle.properties', 'w') as file:
        file.write(filedata)
except:
    error("Failed to overwrite gradle.properties. Please check if the file exists and try again.")


#Rename the main package
try:
    maven_group_split = maven_group.split(".")
    renamed_path = path+'//src//main//java//'+maven_group_split[0]
    os.rename(path+'//src//main//java//net', renamed_path)
    os.rename(renamed_path+'//fabricmc', renamed_path+'//'+maven_group_split[1])
    os.rename(renamed_path+'//'+maven_group_split[1]+'//example', renamed_path+'//'+maven_group_split[1]+'//'+mod_name.lower())
except:
    error("Failed to rename package src/main/java/*yourmavengroup*/*yourmodname*. Please check if the package src/main/java/net/fabricmc/example exists and try again.")


#Open and modify the main class
try:
    with open(path+'//src//main//java//'+maven_group_split[0]+'//'+maven_group_split[1]+'//'+mod_name+'//'+'ExampleMod.java', 'r') as file:
        filedata = file.read()
except:
    error("Failed to open the main class ExampleMod.java. Please check if it exists and if its name is no longer ExampleMod.java, please create an issue on the Github of this project.")
try:
    filedata = filedata.replace('package net.fabricmc.example;', 'package '+maven_group+'.'+mod_name.lower()+';')
    filedata = filedata.replace('modid', mod_name.lower())
    filedata = filedata.replace('ExampleMod', mod_name)
except:
    error("Failed to rename references in the main class ExampleMod.java. Please check the names of the packages and create an issue on the Github of this project.")
try:
    with open(path+'//src//main//java//'+maven_group_split[0]+'//'+maven_group_split[1]+'//'+mod_name+'//'+'ExampleMod.java', 'w') as file:
        file.write(filedata)
except:
    error("Failed to overwrite data on the main class ExampleMod.java. Please create an issue on the Github of this project.")
try:
    os.rename(path+'//src//main//java//'+maven_group_split[0]+'//'+maven_group_split[1]+'//'+mod_name+'//'+'ExampleMod.java', path+'//src//main//java//'+maven_group_split[0]+'//'+maven_group_split[1]+'//'+mod_name+'//'+mod_name+'.java')
except:
    error("Failed to rename the main class ExampleMod.java to *yourmodname*.java. Please create an issue on the Github of this project")


#Open and modify the default mixin class
try:
    with open(path+'//src//main//java//'+maven_group_split[0]+'//'+maven_group_split[1]+'//'+mod_name+'//'+'mixin//ExampleMixin.java', 'r') as file:
        filedata = file.read()
except:
    error("Failed to open the default mixin class ExampleMixin.java. Please check if it exists and try again.")
try:
    filedata = filedata.replace('package net.fabricmc.example.mixin;', 'package '+maven_group+'.'+mod_name.lower()+'.mixin;')
    filedata = filedata.replace('net.fabricmc.example.ExampleMod', maven_group+'.'+mod_name.lower()+"."+mod_name)
    filedata = filedata.replace('ExampleMod', mod_name)
except:
    error("Failed to rename references in the default mixin class ExampleMixin.java. Please create an issue on the Github of this project")
try:
    with open(path+'//src//main//java//'+maven_group_split[0]+'//'+maven_group_split[1]+'//'+mod_name+'//'+'mixin//ExampleMixin.java', 'w') as file:
        file.write(filedata)
except:
    error("Failed to overwrite the data in the default mixin class ExampleMixin.java. Please create an issue on the Github of this project")


#Open and modify fabric.mod.json
try:
    with open(path+'//src//main//resources//fabric.mod.json', 'r') as file:
        filedata = file.read()
except:
    error("Failed to open fabric.mod.json. Please check if it exists and try again")
try:
    filedata = filedata.replace('modid', mod_name.lower())
    filedata = filedata.replace('Example Mod', mod_name)
    filedata = filedata.replace('This is an example description! Tell everyone what your mod is about!', mod_description)
    filedata = filedata.replace('Me!', mod_creator)
    filedata = filedata.replace('net.fabricmc.example.ExampleMod', maven_group+'.'+mod_name.lower()+'.'+mod_name)
    filedata = filedata.replace('CC0-1.0', mod_creator)
    filedata = filedata.replace('https://fabricmc.net/', mod_homepage)
    filedata = filedata.replace('https://github.com/FabricMC/fabric-example-mod', mod_source)
except:
    error("Failed to rename references in fabric.mod.json. Please create an issue on the Github of this project")
try:
    with open(path+'//src//main//resources//fabric.mod.json', 'w') as file:
        file.write(filedata)
except:
    error("Failed to overwrite the data in fabric.mod.json. Please create an issue on the Github of this project")


#Open and modify 'modid.mixins.json'
try:
    with open(path+'//src//main//resources//modid.mixins.json', 'r') as file:
        filedata = file.read()
except:
    error("Failed to open modid.mixins.json Please check if it exists and try again")
try:
    filedata = filedata.replace('net.fabricmc.example.mixin', maven_group+"."+mod_name.lower()+".mixin")
except:
    error("Failed to rename references in modid.mixins.json. Please create an issue on the Github of this project")
try:
    with open(path+'//src//main//resources//modid.mixins.json', 'w') as file:
        file.write(filedata)
except:
    error("Failed to overwrite the data in modid.mixins.json. Please create an issue on the Github of this project")


#Rename 'modid' to the user's chosen modid
try:
    os.rename(path+'//src//main//resources//modid.mixins.json', path+'//src//main//resources//'+mod_name.lower()+'.mixins.json')
except:
    error("Failed to rename modid.mixins.json to *yourmodname*.mixins.json. Please check your mod's name and try again.")
try:
    os.rename(path+'//src//main//resources//assets//modid', path+'//src//main//resources//assets//'+mod_name.lower())
except:
    error("Failed to rename the folder modid to your mod's name. Please check your mod's name and the 'modid' directory and try again.")


#Create a custom README for the user's mod
import os
try:
    os.remove(path+'//README.md')
except:
    error("Failed to delete README.md. Please create an issue on the Github of this project")
try:
    with open(path+'//README.md', 'w') as f:
        f.write('# '+mod_name+'\r\n![Java 16](https://img.shields.io/badge/language-Java%2016-9B599A.svg?style=flat-square)\r![Mod loader: Fabric](https://img.shields.io/badge/modloader-fabric-blue?style=flat-square)\r\n'+'### '+mod_description+'\r\n\r\n## License\r\nThis mod is available under the '+mod_license+' license.')
except:
    error("Failed to create README.md. Please create an issue on the Github of this project")
try:
    os.remove(path+'//LICENSE')
except:
    error("Failed to remove the LICENSE file. Please create an issue on the Github of this project")


#Delete the .github directory
try:
    gitdir_path = path+'//.github'
    shutil.rmtree(gitdir_path)
except:
    error("Failed to delete the .github directory. Please check if it exists and please create an issue on the Github of this project")