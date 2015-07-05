#!/usr/bin/python
# -*- coding: utf-8 -*-

import shutil

def scaleMonster(chooseScale, chooseBody, choosePos, path, pathbase):

    in_file = open(pathbase + "base_monster.wrl", "r")
    out_file = open(path + "/" + "monster.wrl", "w")

    for line in in_file:

        if "#rotation_monster_body" in line:
            if choosePos == 2:
                line = "\trotation 0 1 0 0.1745 #rotation_monster_body\n"

        elif "#rotation_monster" in line:

            if choosePos == 5: #attack1
                line = "\t\t\trotation 1 0 0 0.20 #rotation_monster\n"

            elif choosePos == 6: #attack3
                line = "\t\t\trotation 1 0 0 0.15 #rotation_monster\n"   

            elif choosePos == 2:
                line = "\t\t\trotation 1 0 0 -0.18 #rotation_monster\n"         

        elif "#scale_monster" in line:
            if chooseScale == 0:
                line = "\t\t\tscale 0.4 0.4 0.4 #scale_monster\n"

            elif chooseScale == 1:
                line = "\t\t\tscale 1 1 1 #scale_monster\n"
                
            else:
                line = "\t\t\tscale 1.5 1.5 1.5 #scale_monster\n"

        elif "#shape_body" in line:
            if chooseBody == 1:
                line = "\t\t\t\t\t\t#shape_body"

        elif "#texture_monster" in line:
            if chooseBody == 1:
                line = "\t\t\tshininess .07 diffuseColor .44 .1 0 specularColor 1 .68 .51 ambientIntensity .0833 emissiveColor .15 .13 .06 #texture_monster\n\n"

        elif "#pos_type_weapon" in line:
            if choosePos == 0:
                line = " #pos_type_weapon\n"

                # Poner escudo 2

            elif choosePos == 1 and chooseBody == 0:
                line = "Inline { url \"escudo.wrl\" } #pos_type_weapon\n"
                shutil.copy2(pathbase + "base_escudo.wrl", path + "/" + "escudo.wrl")  

            elif choosePos == 1 and chooseBody == 1:
                line = "Inline { url \"field.wrl\" } #pos_type_weapon\n"
                shutil.copy2(pathbase + "base_field.wrl", path + "/" + "field.wrl")  


            elif choosePos == 2 and chooseBody == 0:
                line = " #pos_type_weapon\n"

            elif choosePos == 2 and chooseBody == 1:
                line = " #pos_type_weapon\n"

            elif choosePos == 3 and chooseBody == 0:
                line = " #pos_type_weapon\n"

            elif choosePos == 3 and chooseBody == 1:
                line = " #pos_type_weapon\n"

                
            elif choosePos == 4 and chooseBody == 0: #attack0
                line = "Inline { url \"espada.wrl\" } #pos_type_weapon\n"

            elif choosePos == 5 and chooseBody == 0: #attack1
                line = "Inline { url \"espada.wrl\" } #pos_type_weapon\n"

            elif choosePos == 4 and chooseBody == 1: #attack0
                line = "Inline { url \"lanza.wrl\" } #pos_type_weapon\n"

            elif choosePos == 5 and chooseBody == 1: #attack1
                line = "Inline { url \"lanza.wrl\" } #pos_type_weapon\n"  

            elif choosePos == 6 and chooseBody == 0: #attack2
                line = "Inline { url \"ball.wrl\" } #pos_type_weapon\n"          
            
            elif choosePos == 6 and chooseBody == 1: #attack2
                line = "Inline { url \"laser.wrl\" } #pos_type_weapon\n"  


        out_file.write(line)




    in_file.close()
    out_file.close()

def posMonster(chooseBody, choosePos, path, pathbase):

    in_file = open(pathbase + "base_arms.wrl", "r")
    out_file = open(path + "/" + "arms.wrl", "w")

    for line in in_file:
        if "#pos_type_left" in line:
            if choosePos == 0:
                line = "\t\trotation 1 0 0 0.54 #pos_type_left\n" 

            elif choosePos == 2:
                line = "\t\trotation 1 0 0 1.24 #pos_type_left\n"

            elif choosePos == 1 and chooseBody == 0: #defense0
                line = "\t\trotation 1 0 0 1.578 #pos_type_left\n" 

            elif choosePos == 1 and chooseBody == 1: #defense0
                line = "\t\trotation 1 0 0 1.578 #pos_type_left\n" 

            elif choosePos == 3 and chooseBody == 0:
                line = "\t\trotation 1 0 0 1.24 #pos_type_left\n" 

            elif choosePos == 3 and chooseBody == 1: 
                line = "\t\trotation 1 0 0 1.24 #pos_type_left\n"                

            elif choosePos == 4 and chooseBody == 0: #attack0
                line = "\t\trotation 1 0 0 0.955 #pos_type_left\n"
            elif choosePos == 4 and chooseBody == 1: #attack0
                line = "\t\trotation 1 0 0 3.14 #pos_type_left\n"                
            elif choosePos == 5: #attack1
                line = "\t\trotation 1 0 0 1.955 #pos_type_left\n"
            elif choosePos == 6 and chooseBody == 0: #attack2 - laser
                line = "\t\trotation 1 0 0 1.0 #pos_type_left\n"
            elif choosePos == 6 and chooseBody == 1: #attack2 - laser
                line = "\t\trotation 1 0 0 0.40 #pos_type_left\n"

        elif "#posZero_type_left" in line:
            if choosePos == 3 and chooseBody == 0:
                line = "\t\trotation 0 1 0 3.45 #pos0_type_left\n" 

            elif choosePos == 3 and chooseBody == 1: 
                line = "\t\trotation 0 1 0 3.45 #pos0_type_left\n"

        elif "#pos_type_right" in line: 
            if choosePos == 0:
                line = "\t\trotation 1 0 0 -0.54 #pos_type_right\n"
            elif choosePos == 1 and chooseBody == 0:
                line = "\t\trotation 1 0 0 -1.578 #pos_type_right\n" 

            elif choosePos == 1 and chooseBody == 1: 
                line = "\t\trotation 1 0 0 -1.578 #pos_type_right\n" 

            elif choosePos == 3 and chooseBody == 0:
                line = "\t\trotation 0 1 0 -0.80 #pos_type_right\n" 

            elif choosePos == 3 and chooseBody == 1: 
                line = "\t\trotation 0 1 0 -0.80 #pos_type_right\n"                 

            elif choosePos == 4 and chooseBody == 0: #attack0
                line = "\t\trotation 1 0 0 -1.24 #pos_type_right\n"
            elif choosePos == 4 and chooseBody == 1: #attack0
                line = "\t\trotation 1 0 0 -1.24 #pos_type_right\n"                
            elif choosePos == 5: #attack1
                line = "\t\trotation 1 0 0 0.45 #pos_type_right\n"
            elif choosePos == 6 and chooseBody == 0: #attack2 - laser
                line = "\t\trotation 1 0 0 -1.58 #pos_type_right\n"
            elif choosePos == 6 and chooseBody == 1: #attack2 - laser
                line = "\t\trotation 1 0 0 -0.40 #pos_type_right\n"   

        elif "#trans_type_right" in line:
            if choosePos == 3 and chooseBody == 0:
                line = "\t\t#trans_type_right\n" 

            elif choosePos == 3 and chooseBody == 1: 
                line = "\t\t#trans_type_right\n"

        elif "#pos2_type_right" in line:
            if choosePos == 3 and chooseBody == 0:
                line = "\t\t\trotation 1 0 0 -1.7   #pos2_type_right\n" 

            elif choosePos == 3 and chooseBody == 1: 
                line = "\t\t\trotation 1 0 0 -1.7   #pos2_type_right\n"  

        elif "#trans2_type_right" in line:
            if choosePos == 3 and chooseBody == 0:
                line = "\t\t\ttranslation -1 16 12  #trans2_type_right\n" 

            elif choosePos == 3 and chooseBody == 1: 
                line = "\t\t\ttranslation -1 16 12  #trans2_type_right\n"  


        elif "#texture_monster" in line:
            if chooseBody == 1:
                line = "\t\t\tshininess .07 diffuseColor .44 .1 0 specularColor 1 .68 .51 ambientIntensity .0833 emissiveColor .15 .13 .06 #texture_monster\n\n"


        out_file.write(line)




    in_file.close()
    out_file.close()

def ornamentMonster(chooseBody, path, pathbase):

    in_file = open(pathbase + "base_ornaments.wrl", "r")
    out_file = open(path + "/" + "ornaments.wrl", "w")

    for line in in_file:

        if "#body_type" in line:
            if chooseBody == 0:
                line = "\t\t\t\tsize 5 0.8 3 #body_type\n"

            elif chooseBody == 1:
                line = "\t\t\t\tsize 2.5 0.8 3 #body_type\n"

        if "#spikes_body_t" in line:
            if chooseBody == 0:
                line = "\ttranslation 0 14 5.5 #spikes_body_t\n"

            elif chooseBody == 1:
                line = "\ttranslation 0 14 4.5 #spikes_body_t\n"

        if "#spikes_body_h" in line:
            if chooseBody == 0:
                line = "\t\t\t\theight 1 #spikes_body_h\n"

            elif chooseBody == 1:
                line = "\t\t\t\theight 2.5 #spikes_body_h\n"

        if "#horn_body" in line:
            line = line.lstrip("\t")

            h1, h2, h3, h4, h5, h6 = line.split(" ",5)

            if chooseBody == 0:
                h2 = float(h2) + 1.0
                h5 = float(h5) + 1.0

            elif chooseBody == 1:
                h2 = float(h2) + 5.0
                h5 = float(h5) + 6.0
    
            line = "\t\t\t\t\t" + h1 + " " + str(h2) +  " " + h3 +  " " + h4 +  " " + str(h5) +  " " + h6

        if "#texture_monster" in line:
            if chooseBody == 1:
                line =  "\t\t\tdiffuseColor 0 0 0 emissiveColor 0 0 1 ambientIntensity 0 specularColor 0 .92 1 shininess .03 #texture_monster\n\n"

        out_file.write(line)


    in_file.close()
    out_file.close()

def nTail(chooseBody, chooseTail, choosePos, path, pathbase):
    
    in_file = open(pathbase + "base_cola.wrl", "r")
    out_file = open(path + "/" + "cola.wrl", "w")

    for line in in_file:
        if "#tail_n1" in line:
            if chooseTail == 0:
                line = "#tail_n1\n"

            elif chooseTail == 1:
                line = "Transform { rotation 0 1 0 0.6109 translation   -1 0 -3 children [ USE TAIL ] } #tail_n1\n"
                
        elif "#tail_n2" in line:
            if chooseTail == 0:
                line = "#tail_n2\n"

            elif chooseTail == 1:
                line = "Transform { rotation 0 1 0 -0.6109 translation   1 0 -3 children [ USE TAIL ] } #tail_n2\n"

        elif "#tail_sp" in line:
            if chooseTail == 0:
                line = "\t\t\t\t\t0 10.75 -5, 0 10.65 -5.5, 0 10.60 -8,  0 10.60 -8.5 #tail_sp"
            if chooseTail == 1:
                line = "\t\t\t\t\t0 10.75 -6 #tail_sp"                

        elif "#tail_sc" in line:
            if chooseTail == 0:
                line = "\t\t\t\t\t0.25 0.25,  0.25 0.25, 0.10 0.10, 0 0 #tail_sc"
            if chooseTail == 1:
                line = "\t\t\t\t\t0 0 #tail_sc"      

        elif "#pos_tail_rot" in line:
            if choosePos == 5:
                line = "rotation 1 0 0 -0.45 #pos_tail_rot\n"  

        elif "#pos_tail_tras" in line:
            if choosePos == 5:
                line  = "translation    0 2 2.5 #pos_tail_tras\n"

        elif "#texture_monster" in line:
            if chooseBody == 1:
                line = "\t\t\tshininess .07 diffuseColor .44 .1 0 specularColor 1 .68 .51 ambientIntensity .0833 emissiveColor .15 .13 .06 #texture_monster\n\n"


        out_file.write(line)


    in_file.close()
    out_file.close()

    
def legLength(chooseScale, chooseBody, chooseLength, chooseGround, choosePos, path, pathbase):

    in_file = open(pathbase + "base_legs.wrl", "r")
    out_file = open(path + "/" + "legs.wrl", "w")

    for line in in_file:
        if "#length_legs" in line:
            line = line.lstrip("\t")
            p1, p2, p3 = line.split(" ",2)

            if chooseLength == 0:
                p1 = float(p1) + 1.0

            elif chooseLength == 1:
                p1 = float(p1) + 3.0

            else:
                p1 = float(p1) + 5.0
                
            line = "\t\t\t\t\t" + str(p1) + " " + p2 +  " " + p3

        elif "#ground_type" in line:

            line = line.lstrip("\t")
            g1, g2, g3 = line.split(" ",2)

            if chooseGround == 0:
                g1 = float(g1) + 0.7
                g2 = float(g2) + 0.7


            elif chooseGround == 1:
                g1 = float(g1) + 0.25
                g2 = float(g2) + 0.25

            else:
                g1 = float(g1) + 0.0
                g2 = float(g2) + 0.0
                
            line = "\t\t\t\t\t" + str(g1) + " " + str(g2) +  " " + g3

        elif "#scale_monster" in line:
            if chooseScale == 0:
                line = "\t\t\tscale 0.4 0.4 0.4 #scale_monster\n"

            elif chooseScale == 1:
                line = "\t\t\tscale 1 1 1 #scale_monster\n"
                
            else:
                line = "\t\t\tscale 1.5 1.5 1.5 #scale_monster\n"

        elif "#rotation_legs" in line:
            if choosePos == 5:
                line = "\t\t\trotation 0 0 1 -0.3927 #rotation_legs\n" # attack_salt

        elif "#leg_front" in line:
            if choosePos == 2:
                line = "\t\t\trotation 0 0 1 0.30 #leg_front\n" # defense1           

        elif "#texture_monster" in line:
            if chooseBody == 1:
                line = "\t\t\tshininess .07 diffuseColor .44 .1 0 specularColor 1 .68 .51 ambientIntensity .0833 emissiveColor .15 .13 .06 #texture_monster\n\n"

        elif "#trans_leg_back" in line:
            if choosePos == 5:
                line = "\ttranslation 0 1 2 #trans_leg_back"



        out_file.write(line)

    in_file.close()
    out_file.close()


def word(chooseBody, choosePos, path, pathbase):

    if chooseBody == 0 and choosePos == 6:
        in_file = open(pathbase + "base_ball.wrl", "r")
        out_file = open(path + "/" + "ball.wrl", "w") 
        shutil.copy2(pathbase + "fire.jpg", path + "/" + "fire.jpg") 

        for line in in_file:
            out_file.write(line)  

    elif chooseBody == 1 and choosePos == 6:
        in_file = open(pathbase + "base_laser1.wrl", "r")
        out_file = open(path + "/" + "laser.wrl", "w") 
        #shutil.copy2(pathbase + "fire.jpg", path + "/" + "fire.jpg") 

        for line in in_file:
            out_file.write(line)      

    elif chooseBody == 0:
        in_file = open(pathbase + "base_espada.wrl", "r")
        out_file = open(path + "/" + "espada.wrl", "w")

        for line in in_file:
            if "#pos_word_rot" in line:
                if choosePos == 5:
                    line = "\trotation  1 0 0 -0.2 #pos_word_rot\n"
                if choosePos == 4:
                    pass

            if "#pos_word_tras" in line:
                if choosePos == 5:
                    line = "\ttranslation   -11 17.5 10 #pos_word_tras\n"
                if choosePos == 4:
                    pass

            out_file.write(line)

    elif chooseBody == 1:
        in_file = open(pathbase + "base_lanza.wrl", "r")
        out_file = open(path + "/" + "lanza.wrl", "w")

        for line in in_file:
            if "#pos_lanza_rot" in line:
                if choosePos == 5:
                    line = "\trotation  1 0 0 -0.2 #pos_lanza_rot\n"
                if choosePos == 4:
                    line = "\trotation  1 0 0 1.5708 #pos_lanza_rot\n"

            if "#pos_lanza_tras" in line:
                if choosePos == 5:
                    line = "\ttranslation   -11 18.5 9.5 #pos_lanza_tras\n"
                if choosePos == 4:
                    line = "\ttranslation -11 25.5 0 #pos_lanza_tras\n"

            out_file.write(line)


    in_file.close()
    out_file.close()




def generateFiles(path, path2):
    #shutil.copy2(path + "base_escudo.wrl", path2 + "/" + "escudo.wrl")  
    #shutil.copy2(path + "base_espada.wrl", path2 + "/" + "espada.wrl") 
    shutil.copy2(path + "base_views.wrl", path2 + "/" + "views.wrl")  
    #shutil.copy2(path + "space.jpg", path2 + "/" + "space.jpg")  