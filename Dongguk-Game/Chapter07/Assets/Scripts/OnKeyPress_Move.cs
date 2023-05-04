using System.Collections;
using System.Collections.Generic;
using Unity.VisualScripting;
using UnityEngine;

public class OnKeyPress_Move : MonoBehaviour
{
    public float speed = 2;
    public float jumppower = 8;

    float vx = 0;
    bool leftFlag = false;
    bool pushFlag = false;
    bool jumpedFlag = false;  
    bool groundFlag = false;

    string nowMode = "";

    public string idleAnime = "";
    public string runAnime = "";
    public string jumpAnime = "";

    Rigidbody2D rbody;

    // Start is called before the first frame update
    void Start()
    {
        rbody = GetComponent<Rigidbody2D>();
        rbody.constraints = RigidbodyConstraints2D.FreezeRotation;
    }

    // Update is called once per frame
    void Update()
    {
        vx = 0;
        nowMode = idleAnime;
        if (Input.GetKey("right"))
        {
            vx = speed;
            leftFlag = false;
            nowMode = runAnime;
        }
        if (Input.GetKey("left"))
        {
           vx = -speed;
           leftFlag = true;
            nowMode = runAnime;
        }
        if (Input.GetKey("space") && groundFlag)
        {
            if (pushFlag == false)
            {
                jumpedFlag = true;
                pushFlag = true;
                nowMode = jumpAnime;
            }
        } else
        {
            pushFlag = false;
        }
        if (groundFlag == false)
        {
            nowMode = jumpAnime;
        }
    }

    private void FixedUpdate()
    {
        rbody.velocity = new Vector2 (vx, rbody.velocity.y);
        this.GetComponent<Animator>().Play(nowMode);
        this.GetComponent<SpriteRenderer>().flipX = leftFlag;
        if (jumpedFlag)
        {
            jumpedFlag =false;
            rbody.AddForce(new Vector2(0,jumppower), ForceMode2D.Impulse);
        }
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
