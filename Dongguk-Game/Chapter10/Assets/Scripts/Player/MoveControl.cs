using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MoveControl : MonoBehaviour
{
    [SerializeField] private KeyCode[] InputMove;

    [SerializeField] private float speed;
    [SerializeField] private float jumpPower;
    private float vx = 0;

    [SerializeField] private string runMoving = "";
    [SerializeField] private string jumpMoving = "";
    [SerializeField] private string stay = "";

    private string nowMove = "";
    private bool groundFlag = false;
    private bool pushFlag = false;
    private bool jumpFlag = false;
    private bool leftFlag = false;

    Rigidbody2D r2d;
    
    Player player;
    private void Start()
    {
        r2d = GetComponent<Rigidbody2D>();
    }

    void Update()
    {
        vx = 0;
        nowMove = stay;
        if (Input.GetKey(InputMove[0]))
        {
            vx = -speed;
            nowMove = runMoving;
            leftFlag = true;
        }
        if (Input.GetKey(InputMove[1]))
        {
            vx = speed;
            nowMove = runMoving;
            leftFlag = false;
        }
        if (Input.GetKey(InputMove[2]) && groundFlag)
        {
            if (!pushFlag)
            {
                jumpFlag = true;
                pushFlag = true;
            }
        } else
        {
            pushFlag = false;
        }
        if (!groundFlag)
        {
            nowMove = jumpMoving;
        }
    }


    private void FixedUpdate()
    {
        r2d.velocity = new Vector2(vx, r2d.velocity.y);
        this.GetComponent<SpriteRenderer>().flipX = leftFlag;
        this.GetComponent<Animator>().Play(nowMove);

        if (jumpFlag)
        {
            jumpFlag = false;
            r2d.AddForce(new Vector2(0, jumpPower), ForceMode2D.Impulse);
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
