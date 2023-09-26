import java.time.Duration;

public class Exercice2 {
    public static void main(String[] args) {
        Article[] articles = new Article[]{
                new Livre(1, "Le Petit Prince", 9.99f, 9782070408504L, 97, "Antoine de Saint-Exupéry"),
                new Article(2, "Marshall Monitor II ANC", 299.99f),
                new Article(3, "Mac Mini M2", 599.99f),
                new Disque(4, "Matrix", 9.99f, Duration.parse("PT2H16M"), "Les Wachowski")
        };

        for (Article article: articles) {
            if (article instanceof Livre livre) {
                System.out.println(livre.getDesignation() + " (" + livre.getAuteur()+ ") a " + livre.getPages() + " pages, coûte " + livre.getPrix() + " a pour ISBN " + livre.getIsbn() + " et pour reference " + livre.getReference());
            } else if (article instanceof Disque disque) {
                System.out.println(disque.getDesignation() + " (" + disque.getRealisateur() + ") dure " + disque.getDureeAsString() + ", coûte " + disque.getPrix() + " et a pour référence " + disque.getReference());
            } else {
                System.out.println(article.getDesignation() + " coûte " + article.getPrix() + " et a pour référence " + article.getReference());
            }
        };
    }
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
    String auteur;

    public Livre(int reference, String designation, float prix, long isbn, int pages, String auteur) {
        super(reference, designation, prix);
        this.isbn = isbn;
        this.pages = pages;
        this.auteur = auteur;
    }

    public int getPages() { return pages; }
    public long getIsbn() { return isbn; }
    public String getAuteur() { return auteur; }
}

class Disque extends Article {
    Duration duree;
    String realisateur;

    public Disque(int reference, String designation, float prix, Duration duree, String realisateur) {
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
    public String getRealisateur() { return realisateur; }
}