using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class GameCounter : MonoBehaviour
{
    public static int count;
    public static int heart;

    public int startCount = 0;
    public int startHeart = 100;

    public int endCount = 10;

    public string gameoverScene;
    public string gameclearScene;


    private void Start()
    {
        count = startCount;
        heart = startHeart;
    }

    private void Update()
    {
        if (count >= endCount)
        {
            SceneManager.LoadScene(gameclearScene);
        }
        if (heart <= 0)
        {
            SceneManager.LoadScene(gameoverScene);
        }
    }
}
