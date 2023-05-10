using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class Enemy : MonoBehaviour
{
    [SerializeField] private string gameoverScene;

    private void OnTriggerEnter2D(Collider2D collision)
    {
        if (collision.gameObject.name == "player")
        {
            SceneManager.LoadScene(gameoverScene);
        }
    }
}
