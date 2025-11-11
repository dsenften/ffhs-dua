package openai;

import com.google.gson.JsonArray;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import lombok.extern.log4j.Log4j2;
import org.apache.hc.client5.http.classic.methods.HttpPost;
import org.apache.hc.client5.http.impl.classic.CloseableHttpClient;
import org.apache.hc.client5.http.impl.classic.HttpClients;
import org.apache.hc.core5.http.io.HttpClientResponseHandler;
import org.apache.hc.core5.http.io.entity.StringEntity;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.stream.Collectors;

@Log4j2
public class OpenAIClient {

    // Name der Umgebungsvariable, in der der API-Schlüssel gespeichert ist
    private static final String API_KEY = "OPENAI_API_KEY";
    private static final String ENDPOINT = "https://api.openai.com/v1/chat/completions";

    public static void main(String[] args) {

        // API-Schlüssel aus der Umgebungsvariable lesen
        String apiKey = System.getenv(API_KEY);
        if (apiKey == null || apiKey.isEmpty()) {
            System.err.println("API-Schlüssel nicht gefunden. Bitte setze die Umgebungsvariable " + API_KEY);
            return;
        }

        String prompt = "Erkläre, wie ein QuickSort-Algorithmus funktioniert.";

        try (CloseableHttpClient httpClient = HttpClients.createDefault()) {

            // API-Anfrage erstellen
            HttpPost request = getHttpPost(apiKey, prompt);

            // ResponseHandler zur Verarbeitung der Antwort
            HttpClientResponseHandler<String> responseHandler = response -> {
                int status = response.getCode();
                if (status >= 200 && status < 300) {
                    // Lese die Antwort als String
                    try (BufferedReader reader = new BufferedReader(
                            new InputStreamReader(response.getEntity().getContent(), StandardCharsets.UTF_8))) {
                        return reader.lines().collect(Collectors.joining(System.lineSeparator()));
                    }
                } else {
                    throw new RuntimeException("Unerwarteter Statuscode: " + status);
                }
            };

            // API-Aufruf ausführen und Antwort verarbeiten
            String responseBody = httpClient.execute(request, responseHandler);

            // Antwort in JSON-Format umwandeln anschliessend den Inhalt (`content`) ausgeben
            JsonObject responseJson = JsonParser.parseString(responseBody).getAsJsonObject();
            String content = responseJson.getAsJsonArray("choices")
                    .get(0)
                    .getAsJsonObject()
                    .getAsJsonObject("message")
                    .get("content").getAsString();
            System.out.println(content);


        } catch (Exception e) {
            log.error("API-Aufruf fehlgeschlagen: {}", e.getMessage());
        }
    }

    private static HttpPost getHttpPost(String apiKey, String prompt) {
        HttpPost request = new HttpPost(ENDPOINT);
        request.addHeader("Content-Type", "application/json");
        request.addHeader("Authorization", "Bearer " + apiKey);

        // JSON-Anfragekörper erstellen
        JsonObject json = new JsonObject();
        json.addProperty("model", "gpt-4o");

        // Erstelle das messages-Array korrekt
        JsonArray messages = new JsonArray();
        JsonObject userMessage = new JsonObject();
        userMessage.addProperty("role", "user");
        userMessage.addProperty("content", prompt);
        messages.add(userMessage);

        json.add("messages", messages);
        json.addProperty("max_tokens", 100);

        StringEntity entity = new StringEntity(json.toString());
        request.setEntity(entity);

        return request;
    }
}
