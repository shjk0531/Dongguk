using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class OnMouseDownSwitchScene : MonoBehaviour
{
    [SerializeField] private string sceneName;

    private void OnMouseDown()
    {
        Debug.Log("MouseDown");
        SceneManager.LoadScene(sceneName);
    }
}
