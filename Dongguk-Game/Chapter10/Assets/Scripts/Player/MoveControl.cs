using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MoveControl : MonoBehaviour
{
    [SerializeField] private KeyCode[] InputMove;

    [SerializeField] private float speed;
    private float vx = 0;

    [SerializeField] private string leftMoving = "";
    [SerializeField] private string rightMoving = "";
    [SerializeField] private string stay = "";
    private string nowMove = "";

    Rigidbody2D r2d;
    

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
            nowMove = leftMoving;
        }
        if (Input.GetKey(InputMove[1]))
        {
            vx = speed;
            nowMove = rightMoving;
        }
    }


    private void FixedUpdate()
    {
        r2d.velocity = new Vector2(vx, 0);
        this.GetComponent<Animator>().Play(nowMove);
    }

}
