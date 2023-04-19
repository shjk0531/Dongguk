using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class OnMouseClick_Boss : MonoBehaviour
{
    System.Random rand = new System.Random();
    float count = 0;
    public float speed = 5;
    public float height = 10;
    public int maxDelay = 20;

    int delay = 0;

    public string showObjectName = "";

    GameObject showObject;

    // Start is called before the first frame update
    void Start()
    {
        showObject = GameObject.Find(showObjectName);
        showObject.SetActive(false);

        print("hide showObject gameClear");

        count = 0;
        delay = rand.Next(maxDelay * 10);

    }


    private void FixedUpdate()
    {
        if (count >= delay)
        {
            if (count <= delay + height)
            {
                this.transform.Translate(0, speed / 50, 0);
            }
            if (count >= delay + height && count <= delay + height * 2)
            {
                this.transform.Translate(0, -speed / 50, 0);
            }
            if (count >= delay + height * 2)
            {
                this.transform.Translate(0, 0, 0);
                count = 0;
                delay = rand.Next(maxDelay * 10);
            }
        }

        count++;
    }

    private void OnMouseDown()
    {
        Time.timeScale = 0;
        showObject.SetActive(true);
        this.gameObject.SetActive(false);
    }
}
