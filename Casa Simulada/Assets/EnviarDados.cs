using UnityEngine;
using UnityEngine.Networking;
using System.Collections;

public class EnviarDados : MonoBehaviour
{
    [Header("Configuração do Circuito")]
    public string circuito = "cozinha";
    public string dispositivoId = "meu_dispositivo_unico"; // <-- NOVO CAMPO
    public float wattage = 1400f;
    
    private bool isOn = false;

    // Esta é a função que o Player chama
    public void ToggleState()
    {
        isOn = !isOn;
        float currentWattage = isOn ? wattage : 0f;
        
        Debug.Log($"Toggle {dispositivoId}: {currentWattage}W"); // Log para debug
        
        StartCoroutine(SendData(circuito, dispositivoId, currentWattage));
    }

    IEnumerator SendData(string circuitoId, string devId, float valor)
    {
        WWWForm form = new WWWForm();
        form.AddField("circuito", circuitoId);
        form.AddField("dispositivo_id", devId); // <-- NOVO ENVIO
        form.AddField("wattage", valor.ToString());

        using (UnityWebRequest www = UnityWebRequest.Post("http://127.0.0.1:5000/update", form))
        {
            yield return www.SendWebRequest();

            if (www.result != UnityWebRequest.Result.Success)
            {
                Debug.Log("Erro ao enviar dados: " + www.error);
            }
            else
            {
                Debug.Log("Dados enviados para a API!");
            }
        }
    }
}
