using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class getScore : MonoBehaviour
{
    [SerializeField] private int clearScore;
    private int score;
    [SerializeField] private string clearScene;

    private void Start()
    {
        score = 0;
    }

    private void Update()
    {
        if (score >= clearScore)
        {
            SceneManager.LoadScene(clearScene);
        }
    }

    private void OnTriggerEnter2D(Collider2D collision)
    {
        if (collision.gameObject.GetComponent<ScoreObject>())
        {
            score += 1;
            Destroy(collision.gameObject);
            Debug.Log(score);
        }
    }
}
