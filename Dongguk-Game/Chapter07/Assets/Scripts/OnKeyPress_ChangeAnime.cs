using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class OnKeyPress_ChangeAnime : MonoBehaviour
{
    public string upAnime = "";
    public string downAnime = "";
    public string rightAnime = "";
    public string leftAnime = "";

    string nowMode = "";
    string oldMode = "";

    // Start is called before the first frame update
    void Start()
    {
        nowMode = downAnime;
        oldMode = downAnime;
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown("up"))
        {
            nowMode = upAnime;
        }
        if (Input.GetKeyDown("down"))
        {
            nowMode = downAnime;
        }
        if (Input.GetKeyDown("right"))
        {
            nowMode = rightAnime;
        }
        if (Input.GetKeyDown("left"))
        {
            nowMode = leftAnime;
        }
    }

    private void FixedUpdate()
    {
        if (nowMode != oldMode)
        {
            oldMode = nowMode;
            Animator animator = this.GetComponent<Animator>();
            animator.Play(nowMode);
        }
    }
}
