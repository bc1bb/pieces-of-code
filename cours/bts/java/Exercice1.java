import java.util.ArrayList;
import java.util.List;

public class Exercice1 {
    public static void main(String[] args) {
        String[] adressesMail = new String[]{ "severine@gmail.com", "eric@yahoo.fr", "jeremie@free.fr", "jacky@gmail.com", "patrice@gmail.com", "lisa@free.fr", "bernard@free.fr", "bob@gmail.com", "berenice@yahoo.fr" };
        List<Fournisseur> fournisseurs = new ArrayList<Fournisseur>();
        int totalUtilisateur = 0;

        fournisseurs.add(new Fournisseur("Google", 0, "gmail.com"));
        fournisseurs.add(new Fournisseur("Yahoo", 0, "yahoo.fr"));
        fournisseurs.add(new Fournisseur("Free", 0, "free.fr"));

        for (String adresseMail: adressesMail) {
            totalUtilisateur++;
            String fournisseurMail = adresseMail.substring(adresseMail.indexOf("@") + 1);

            for (Fournisseur fournisseur: fournisseurs) {
                if (fournisseurMail.equals(fournisseur.getAdresse())) {
                    fournisseur.ajouterUtilisateur();
                }
            }
        }

        for (Fournisseur fournisseur: fournisseurs) {
            int pourcentage = fournisseur.getUtilisateurs() * 100 / totalUtilisateur;

            System.out.println("Le fournisseur " + fournisseur.getNom() + " a " + fournisseur.getUtilisateurs() + " utilisateurs dans le tableau soit " + pourcentage + "% des utilisateurs.");
        }
    }
}

class Fournisseur {
    public String nom;
    public int utilisateurs;
    public String adresse;

    public Fournisseur(String nom, int utilisateurs, String adresse) {
        this.nom = nom;
        this.utilisateurs = utilisateurs;
        this.adresse = adresse;

        // L'objet est retourné directement
    }

    public String getNom() { return nom; }
    public String getAdresse() { return adresse; }
    public int getUtilisateurs() { return utilisateurs; }

    public void ajouterUtilisateur() { this.utilisateurs++; }
}