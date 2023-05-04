using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ClearJump : MonoBehaviour
{
    public float jumppower = 8;
    public int jumpcount = 50;
    int count = 0;
    public string jumpAnime = "";
    public string idleAnime = "";

    string nowMode = "";

    bool jumpFlag = false;
    bool groundFlag = false;

    Rigidbody2D rbody;
    // Start is called before the first frame update
    void Start()
    {
        rbody = GetComponent<Rigidbody2D>();
        rbody.constraints = RigidbodyConstraints2D.FreezeRotation;

        count = 0;
    }

    // Update is called once per frame
    void Update()
    {
        nowMode = idleAnime;
        count += 1;
        if (count > jumpcount && groundFlag)
        {
            jumpFlag = true;
            count = 0;
        }
    }

    private void FixedUpdate()
    {
        if (jumpFlag)
        {
            jumpFlag = false;
            nowMode = jumpAnime;
            rbody.AddForce(new Vector2(0, jumppower), ForceMode2D.Impulse);
        } 
        this.GetComponent<Animator>().Play(nowMode);
    }

    private void OnTriggerStay2D(Collider2D collision)
    {
        groundFlag = true;
    }
    private void OnTriggerExit2D(Collider2D collision)
    {
        groundFlag = false;
    }
}
