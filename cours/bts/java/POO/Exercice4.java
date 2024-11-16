import java.time.Duration;
import java.time.LocalDate;
import java.util.ArrayList;

public class Exercice4 {
    public static void main(String[] args) {
        Artiste saintExupery = new Artiste("de Saint-Exupery", "Antoine", LocalDate.of(1900, 6, 29));
        Artiste wachowski = new Artiste("Wachoski", "Freres", LocalDate.of(1967, 12, 29));

        Article[] articles = new Article[]{
                new Livre(1, "Le Petit Prince", 9.99f, 9782070408504L, 97, saintExupery),
                new Livre(2, "Vol de nuit", 9.99f, 9782070346288L, 158, saintExupery),
                new Disque(3, "V for Vendetta", 9.99f, Duration.parse("PT2H12M"), wachowski),
                new Disque(4, "Matrix", 9.99f, Duration.parse("PT2H16M"), wachowski),
        };
        saintExupery.addOeuvre(articles[0]); // Petit Prince
        saintExupery.addOeuvre(articles[1]); // Vol de Nuit
        wachowski.addOeuvre(articles[2]); // V for Vendetta
        wachowski.addOeuvre(articles[3]); // Matrix

        System.out.println("Antoine de Saint-Exupery a écrit:");

        for (Article article: saintExupery.oeuvres) {
            if (article instanceof Livre livre) {
                System.out.println(livre.getDesignation() + " (" + livre.getAuteur()+ ") a " + livre.getPages() + " pages, coûte " + livre.getPrix() + " a pour ISBN " + livre.getIsbn() + " et pour reference " + livre.getReference());
            } else if (article instanceof Disque disque) {
                System.out.println(disque.getDesignation() + " (" + disque.getRealisateur() + ") dure " + disque.getDureeAsString() + ", coûte " + disque.getPrix() + " et a pour référence " + disque.getReference());
            }
        }

        System.out.println("\nLes Wachoski ont réalisés:");

        for (Article article: wachowski.oeuvres) {
            if (article instanceof Livre livre) {
                System.out.println(livre.getDesignation() + " (" + livre.getAuteur()+ ") a " + livre.getPages() + " pages, coûte " + livre.getPrix() + " a pour ISBN " + livre.getIsbn() + " et pour reference " + livre.getReference());
            } else if (article instanceof Disque disque) {
                System.out.println(disque.getDesignation() + " (" + disque.getRealisateur() + ") dure " + disque.getDureeAsString() + ", coûte " + disque.getPrix() + " et a pour référence " + disque.getReference());
            }
        }
    }
}

class Artiste {
    String nom;
    String prenom;
    LocalDate naissance;
    ArrayList<Article> oeuvres = new ArrayList<Article>();

    public Artiste(String nom, String prenom, LocalDate naissance) {
        this.nom = nom;
        this.prenom = prenom;
        this.naissance = naissance;
    }

    public String asString() { return prenom + " " + nom; }
    public void addOeuvre(Article oeuvre) { this.oeuvres.add(oeuvre); }
}

class Article {
    int reference;
    String designation;
    float prix;

    public Article(int reference, String designation, float prix) {
        this.reference = reference;
        this.designation = designation;
        this.prix = prix;
    }

    public String getDesignation() { return designation; }
    public float getPrix() { return prix; }
    public int getReference() { return reference; }
}

class Livre extends Article {
    long isbn;
    int pages;
    Artiste auteur;

    public Livre(int reference, String designation, float prix, long isbn, int pages, Artiste auteur) {
        super(reference, designation, prix);
        this.isbn = isbn;
        this.pages = pages;
        this.auteur = auteur;
    }

    public int getPages() { return pages; }
    public long getIsbn() { return isbn; }
    public String getAuteur() { return auteur.asString(); }
}

class Disque extends Article {
    Duration duree;
    Artiste realisateur;

    public Disque(int reference, String designation, float prix, Duration duree, Artiste realisateur) {
        super(reference, designation, prix);
        this.duree = duree;
        this.realisateur = realisateur;
    }

    public Duration getDuree() { return duree; }
    public String getDureeAsString() {
        long seconds = this.getDuree().getSeconds();
        int minutes = (int) (seconds / 60);
        int heures = minutes / 60;
        int minutesReel = (int) (minutes - (heures*60));
        return heures + "h " + minutesReel;
    }
    public String getRealisateur() { return realisateur.asString(); }
}