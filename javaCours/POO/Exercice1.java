public class Exercice1 {
    public static void main(String[] args) {
        Article[] articles = new Article[]{
                new Article(1, "Le Petit Prince", 9.99f),
                new Article(2, "Marshall Monitor II ANC", 299.99f),
                new Article(3, "Mac Mini M2", 599.99f)
        };

        for (Article article: articles) {
            System.out.println(article.getDesignation() + " coûte " + article.getPrix() + " et a pour référence " + article.getReference());
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