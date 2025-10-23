using UnityEngine;
using UnityEngine.Networking; // <--- Verifique se esta linha NÃO dá erro
using System.Collections;

public class EnviarDados : MonoBehaviour
{
    public string circuito = "chuveiro";
    public float wattage = 5500f;
    private bool isOn = false;

    // Esta é a função que o Player chama
    public void ToggleState()
    {
        isOn = !isOn;
        float currentWattage = isOn ? wattage : 0f;
        StartCoroutine(SendData(circuito, currentWattage));
    }

    IEnumerator SendData(string circuitoId, float valor)
    {
        WWWForm form = new WWWForm();
        form.AddField("circuito", circuitoId);
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
