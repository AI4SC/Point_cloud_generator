import numpy as np

# Parameter für das Fenster
breite = 1.0  # in Meter
hoehe = 1.5  # in Meter
tiefe = 0.15  # in Meter
profil_breite = 0.05  # Rahmenbreite in Metern
dichte = 0.01



# Funktion zur Generierung eines dichten rechteckigen Profils
def rechteck_profil_dicht(x_start, y_start, x_end, y_end, z_min, z_max, breite, dichte=0.01):
    """
    Generiert eine dichte Punktwolke für ein rechteckiges Profil zwischen zwei Punkten.
    """
    dx = x_end - x_start
    dy = y_end - y_start
    length = np.sqrt(dx**2 + dy**2)
    if length == 0:
        return []

    # Normalisierte Richtung des Profils
    ux, uy = -dy / length, dx / length
    nx, ny = ux * breite / 2, uy * breite / 2  # Versatz für Profilbreite

    # Generiere Punkte entlang der Linie
    num_points = int(length / dichte)
    points = []
    for i in range(num_points + 1):
        t = i / num_points
        x = x_start + t * dx
        y = y_start + t * dy
        for z in np.linspace(z_min, z_max, int((z_max - z_min) / dichte)):
            points.append([x - nx, y - ny, z])
            points.append([x + nx, y + ny, z])

    return points
# Funktion zur Generierung einer dichten Fläche auf der x-y-Ebene  (Fensterscheibe)
def generiere_dichte_flaeche(x_min, x_max, y_min, y_max, z, dichte=0.01):
    """
    Generiert eine dichte Fläche auf der x-y-Ebene.
    """
    points = []
    x_range = np.arange(x_min, x_max + dichte, dichte)
    y_range = np.arange(y_min, y_max + dichte, dichte)
    for x in x_range:
        for y in y_range:
            points.append([x, y, z])
    return points

# Generierung der Punktwolke für das Fenster
punkte_dicht_fenster = []

# Äußere Rahmenpunkte des Fensters (dicht)
punkte_dicht_fenster.extend(rechteck_profil_dicht(-breite / 2 , -hoehe / 2, breite / 2 , -hoehe / 2, -tiefe / 2, tiefe / 2, profil_breite))  # Unten
punkte_dicht_fenster.extend(rechteck_profil_dicht(-breite / 2 , hoehe / 2, breite / 2 , hoehe / 2, -tiefe / 2, tiefe / 2, profil_breite))    # Oben
punkte_dicht_fenster.extend(rechteck_profil_dicht(-breite / 2, -hoehe / 2 - profil_breite/2, -breite / 2, hoehe  / 2 + profil_breite/2, -tiefe / 2, tiefe / 2, profil_breite))  # Links
punkte_dicht_fenster.extend(rechteck_profil_dicht(breite / 2, -hoehe / 2 - profil_breite/2, breite / 2, hoehe  / 2 + profil_breite/2, -tiefe / 2, tiefe / 2, profil_breite))    # Rechts


# Schließende Flächen an den Ecken des Profils, um die Hälfte der Rahmenbreite nach außen verschoben
offset = -profil_breite/2

# Unten - Schließende Fläche bei z = -tiefe / 2 (Unterseite des Rahmens) Check
punkte_dicht_fenster.extend(generiere_dichte_flaeche(-breite / 2 - offset, breite / 2 + offset, -hoehe / 2 - profil_breite/2, -hoehe / 2 + profil_breite/2, -tiefe / 2, dichte))

# Oben - Schließende Fläche bei z = -tiefe / 2 (Oberseite des Rahmens, Unten) Check
punkte_dicht_fenster.extend(generiere_dichte_flaeche(-breite / 2 - offset, breite / 2 + offset, hoehe / 2 - profil_breite/2, hoehe / 2 + profil_breite/2, -tiefe / 2, dichte))

# Links - Schließende Fläche bei z = -tiefe / 2 (linke Seite des Rahmens) Check
punkte_dicht_fenster.extend(generiere_dichte_flaeche(-breite / 2 - profil_breite/2, -breite / 2 + profil_breite/2, -hoehe / 2 - profil_breite - offset, hoehe / 2 + profil_breite/2, -tiefe / 2, dichte))

# Rechts - Schließende Fläche bei z = -tiefe / 2 (rechte Seite des Rahmens) Check
punkte_dicht_fenster.extend(generiere_dichte_flaeche(breite / 2 - profil_breite/2, breite / 2 + profil_breite/2, -hoehe / 2 - profil_breite - offset, hoehe / 2 + profil_breite/2, -tiefe / 2, dichte))

# Unten - Schließende Fläche bei z = tiefe / 2 (Unterseite des Rahmens) Check
punkte_dicht_fenster.extend(generiere_dichte_flaeche(-breite / 2 - offset, breite / 2 + offset, -hoehe / 2 - profil_breite/2, -hoehe / 2 + profil_breite/2, tiefe / 2, dichte))

# Oben - Schließende Fläche bei z = tiefe / 2 (Oberseite des Rahmens, Oben) Check
punkte_dicht_fenster.extend(generiere_dichte_flaeche(-breite / 2 - offset, breite / 2 + offset, hoehe / 2 - profil_breite/2, hoehe / 2 + profil_breite/2, tiefe / 2, dichte))

# Links - Schließende Fläche bei z = tiefe / 2 (linke Seite des Rahmens,Oben) Check
punkte_dicht_fenster.extend(generiere_dichte_flaeche(-breite / 2 - profil_breite/2, -breite / 2 + profil_breite/2, -hoehe / 2 - profil_breite - offset, hoehe / 2 + profil_breite/2, tiefe / 2, dichte))

# Rechts - Schließende Fläche bei z = tiefe / 2 (rechte Seite des Rahmens,Oben) Check
punkte_dicht_fenster.extend(generiere_dichte_flaeche(breite / 2 - profil_breite/2, breite / 2 + profil_breite/2, -hoehe / 2 - profil_breite - offset, hoehe / 2 + profil_breite/2, tiefe / 2, dichte))



# Fläche innerhalb des Rahmens auf der x-y-Ebene bei z = 0  (Fensterscheibe)
punkte_dicht_fenster.extend(generiere_dichte_flaeche(-breite / 2 +profil_breite/2, breite / 2  -profil_breite/2, -hoehe / 2+profil_breite/2, hoehe / 2-profil_breite/2, 0, dichte))

# Entferne Duplikate
punkte_dicht_fenster = np.unique(np.array(punkte_dicht_fenster), axis=0)

# Speichern der Punktwolke in einer PLY-Datei
ply_path_fenster = "Fenster_dichte_Punktwolke.ply"
with open(ply_path_fenster, "w") as ply_file:
    # Header für PLY-Datei
    ply_file.write("ply\n")
    ply_file.write("format ascii 1.0\n")
    ply_file.write(f"element vertex {len(punkte_dicht_fenster)}\n")
    ply_file.write("property float x\n")
    ply_file.write("property float y\n")
    ply_file.write("property float z\n")
    ply_file.write("end_header\n")
    # Punkte schreiben
    for point in punkte_dicht_fenster:
        ply_file.write(f"{point[0]} {point[1]} {point[2]}\n")

print(f"Dichte Punktwolke wurde erfolgreich in '{ply_path_fenster}' gespeichert.")
